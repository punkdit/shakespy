

def status(message):
    document.getElementById('messages').innerHTML = message


def put_debug(*info):
    element = document.getElementById('debug')
    element.innerHTML += ' '.join([str(i)+"<br>" for i in info]) #+ "<br>"

def put_message(*info):
    element = document.getElementById('messages')
    element.innerHTML += ' '.join([str(i)+"<br>" for i in info]) #+ "<br>"


def clear_message():
    element = document.getElementById('messages')
    element.innerHTML = ""



#ws = WebSocket("ws://localhost:9998/echo")
#ws = websocket("ws://localhost:9998/racer")
ws = websocket("ws://arrowtheory.com:9998/racer")

def onopen():
    #ws.send("hi hi hi!")
    put_debug("Connection established")
ws.onopen = onopen
                
def onmessage(evt):
    put_debug("Message is received:")
    data = evt.data
    put_debug(repr(data))

    if data.strip() == "CLEAR" :
        clear_message()
    else:
        put_message(evt.data)

ws.onmessage = onmessage

def onclose():
    put_debug("lost socket connection")
ws.onclose = onclose

button = document.getElementById("entry_button")
text = document.getElementById("entry_text")
def onclick():
    put_debug("sending:")
    put_debug(text.value)
    ws.send(text.value)
    text.value = ""

button.onclick = onclick

                
#ws.onopen = function()
#{
#// Web Socket is connected, send data using send()
#ws.send("Message to send");
#alert("Message is sent...");
#};
#
#ws.onmessage = function (evt) 
#{ 
#var received_msg = evt.data;
#alert("Message is received...");
#};
#
#ws.onclose = function()
#{ 
#// websocket is closed.
#alert("Connection is closed..."); 
#};
#}


