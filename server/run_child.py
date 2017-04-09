#!/usr/bin/env python3

import os, sys, time
import traceback


_print = print
def print(*args, **kw):
    _print(*args, **kw)
    sys.stdout.flush()

_input = input
def input(*args, **kw):
    print(*args, **kw)
    return _input()


path = sys.argv[1]
cmd = sys.argv[2]

sys.path.insert(0, path)

#os.chdir(path)

#print("run_child: reading %s"%cmd)
s = open("%s/%s"%(path, cmd)).read()

#print("run_child: exec")
try:
    exec(s, globals(), globals())
except:
    #print("Exception in user code:")
    #print("-"*60)
    traceback.print_exc(file=sys.stdout)
    #print("-"*60)
    print()
    print()
    time.sleep(1)



