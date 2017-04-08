#!/usr/bin/env python3

import asyncio
import websockets

import sys, os
from subprocess import Popen, PIPE
import _thread

#os.chdir("../games")

mux = asyncio.get_event_loop()



class Manager(object):

    def __init__(self, cmd, websocket):
        proc = Popen(cmd, shell=True, bufsize=0,
              stdin=PIPE, stdout=PIPE, close_fds=True)
        (child_stdout, child_stdin) = (proc.stdout, proc.stdin)
        #print child_stdout
        #print dir(child_stdout)
        print(child_stdout.fileno())
        print(dir(child_stdout))
        self.cmd = cmd
        self.proc = proc
        self.child_stdout = child_stdout
        self.child_stdin = child_stdin
        self.websocket = websocket
        self.running = True
        #self.tid = _thread.start_new_thread(self.read_from_child, ())
        self.data = None
        mux.add_reader(child_stdout.fileno(), self.read_from_child)
        print("%s.__init__ done" % self)

    def __str__(self):
        return "Manager(%r, running=%s)"%(self.cmd, self.running)

    def to_html(self, data):
        #if "CLEAR" not in data:
        #    data = "<pre>%s</pre>" % data
        return data
    
    def read_from_child(self):
        try:
            if self.proc.poll() is None:
                print("readline:")
                #assert self.data is None
                line = self.child_stdout.readline()
                print("Manager.read_from_child: got %d chars"%len(line))
                if len(line)==0:
                    self.cleanup()
                    return
                line = line.decode("utf-8")
                #if line.endswith("\n"):
                #    line = line[:-1]
                line = self.to_html(line)
                print(line)
                result = asyncio.ensure_future(self.websocket.send(line))
                #result.add_done_callback(f)
            else:
                print("exiting thread")
                self.cleanup()
        except:
            mux.stop()
            raise

    def write_to_child(self, s):
        try:
            s = s.replace("\n", "")
            print("writing:", s)
            s = s+"\n"
            data = s.encode("utf-8")
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
            print("websocket.close()")
            result = asyncio.ensure_future(self.websocket.send("CLOSE"))
            self.websocket.close()
            self.websocket = None
        print("%s.cleanup done" % self)


def test():

    async def foo(s):
        print("foo:", s)
    
    m = Manager("./test_racer.py", foo)
    mux.run_forever()



async def connect(websocket, path):

    print("connect!")
    #cmd = "./test_racer.py"
    #cmd = "./Racer.py"
    manager = Manager(cmd, websocket)

    try:
      while manager.running:
        print("recv... {}".format(path))
        data = await websocket.recv()
        manager.write_to_child(data)
    
    except websockets.ConnectionClosed:
        print("lost connection")

    manager.cleanup()

    print("connect done")
    # websocket doesn't close until we get here...



def main():
    
    start_server = websockets.serve(connect, None, 9998)
    mux.run_until_complete(start_server)
    mux.run_forever()


if __name__ == "__main__":

    cmd = sys.argv[1]
    main()




