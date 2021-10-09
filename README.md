# shakespy

How to run
----------

From the directory "server" run the command :

$ ./server.py

You may need to install the websockets package using pip:

$ pip3 install websockets

Then open up the file web/index.html in the browser.
The server.py process will run other python processes
using the run_child.py script. So watch out for zombie
python processes.

If you want to run this on a server somewhere then serve 
shakespy/web on apache, etc.



