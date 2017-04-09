#!/usr/bin/env python3


import sys, os
from subprocess import Popen, PIPE
import asyncio
import websockets
import re


mux = asyncio.get_event_loop()

def popen_child(path):
    assert path.count('/') >= 2
    items = path.split('/')
    stem = '/'.join(items[:-1]) # working directory
    stem = "../games/%s/"%stem
    tail = items[-1] # command to run
    open(stem+tail).close() # check file is there
    assert tail.endswith(".py")
    cmd = "./run_child.py %s %s" % (stem, tail)
    print("popen_child: %r"%cmd)
    proc = Popen(cmd, shell=True, bufsize=0,
          stdin=PIPE, stdout=PIPE, close_fds=True)

    return proc


def rewrite_data(data):
    "replace multiple newlines with SHAKESPY_CLEAR keyword"

    print("rewrite_data: %r"%data)
    MATCH = '\n'*11
    result = ""
    while MATCH in data:
        idx = data.index(MATCH)
        result += data[:idx]
        print("result += %r"%data[:idx])
        jdx = idx + len(MATCH)
        while jdx < len(data) and data[jdx] == '\n':
            jdx += 1
        data = data[jdx:]
        result += '\nSHAKESPY_CLEAR\n'
    result += data
    print("rewrite_data: result: %r"%result)
    return result


class Manager(object):

    _all = set()
    def __init__(self, path, websocket):
        proc = popen_child(path)
        (child_stdout, child_stdin) = (proc.stdout, proc.stdin)
        self.path = path
        self.proc = proc
        self.child_stdout = child_stdout
        self.child_stdin = child_stdin
        self.websocket = websocket
        self.running = True
        self.data = ""
        self.writer = None
        mux.add_reader(child_stdout.fileno(), self.read_from_child)
        Manager._all.add(self)
        print("%s.__init__ done" % self)

    def __str__(self):
        return "Manager(%r, running=%s)"%(self.path, self.running)

    def log(self, msg):
        print("%s: %s" % (self, msg))

    def to_html(self, data):
        #if "SHAKESPY_CLEAR" not in data:
        #    data = "<pre>%s</pre>" % data
        return data

    async def write_to_client(self):
        print("Manager.write_to_client: enter")
        await asyncio.sleep(0.1) # 0.1 seconds timeout
        data = self.data
        self.data = ""
        data = rewrite_data(data)
        print("Manager.write_to_client: send %d chars"%(len(data)))
        await self.websocket.send(data)
        print("Manager.write_to_client: exit")
        self.writer = None

    def queue_write(self, line):
        self.data += line
        if self.writer is not None:
            self.writer.cancel()
        #if self.writer is None:
        self.writer = asyncio.ensure_future(self.write_to_client())
        #result = asyncio.ensure_future(self.websocket.send(line))
        #result.add_done_callback(f)

    def read_from_child(self):
        try:
            if self.proc.poll() is None:
                print("Manager.read_from_child: readline:")
                line = self.child_stdout.readline()
                print("Manager.read_from_child: got %d chars"%len(line))
                if len(line)==0:
                    self.cleanup()
                    return
                line = line.decode("utf-8")
                #if line.endswith("\n"):
                #    line = line[:-1]
                #line = self.to_html(line)
                print("Manager.read_from_child: %r"%line)
                self.queue_write(line)
            else:
                print("Manager.read_from_child: child exit")
                self.cleanup()
        except:
            mux.stop()
            raise
        print("Manager.read_from_child: exit")

    def write_to_child(self, s):
        try:
            s = s.replace("\n", "")
            print("Manager.write_to_child: writing %r" % s)
            s = s+"\n"
            #self.queue_write("> "+s) # echo back to client (Stone doesn't like this...)
            data = s.encode("utf-8") # to binary
            self.child_stdin.write(data)
            self.child_stdin.flush()
        except:
            mux.stop()
            raise

    def cleanup(self):
        print("%s.cleanup" % self)
        if self.running:
            self.proc.kill()
            for i in range(10):
                self.proc.poll()
            self.running = False
            mux.remove_reader(self.child_stdout.fileno())
        if self.websocket is not None:
            print("%s.cleanup: websocket.close()"%self)
            result = asyncio.ensure_future(self.websocket.send("SHAKESPY_CLOSE\n"))
            self.websocket.close()
            self.websocket = None
        if self in Manager._all:
            Manager._all.remove(self)
        print("%s.cleanup done" % self)


def test():

    async def foo(s):
        print("foo:", s)
    
    m = Manager("./test_racer.py", foo)
    mux.run_forever()



async def connect(websocket, path):

    print("server.connect path=%r"%path)
    manager = Manager(path, websocket)

    try:
      while manager.running:
        print("server.connect: recv")
        data = await websocket.recv()
        manager.write_to_child(data)
    
    except websockets.ConnectionClosed:
        print("server.connect: lost connection")

    except:
        print("server.connect: exception")

    manager.cleanup()

    print("server.connect: exit")
    # websocket doesn't close until we get here...



def main():

    print("server.main: enter")
    start_server = websockets.serve(connect, None, 9998)
    mux.run_until_complete(start_server)
    try:
        mux.run_forever()
    finally:
        for manager in list(Manager._all):
            manager.cleanup()
        mux.close()
        print("server.main: exit")


if __name__ == "__main__":

    main()




