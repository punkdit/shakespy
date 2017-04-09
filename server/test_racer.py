#!/usr/bin/env python3

import os, sys
from time import sleep

_print = print
def print(*args, **kw):
    _print(*args, **kw)
    sys.stdout.flush()

i= 0
while 1:

    i += 1
    print( "hi there #%d"%i)
    #sys.stdout.flush()
    for count in range(3):
        sleep(1)
        print( " --- >")
        print( " --- >")


    x = input()

    print( "got %r"%x)


