

def status(message):
    document.getElementById('messages').innerHTML = message


def put_debug(*info):
    element = document.getElementById('debug')
    #element.innerHTML += ' '.join([str(i)+"<br>" for i in info]) #+ "<br>"


message_data = ""

def put_message(*info):
    message_data += ' '.join([str(i) for i in info])
    element = document.getElementById('messages')
    #element.innerHTML += ' '.join([str(i)+"<br>" for i in info]) #+ "<br>"
    element.innerHTML = "<pre>{}</pre>".format(message_data)


def clear_message():
    global message_data
    put_debug("clear_message")
    element = document.getElementById('messages')
    element.innerHTML = ""
    message_data = ""


element = document.getElementById('messages')
element.style.backgroundColor = "lightgrey"


#ws = WebSocket("ws://localhost:9998/echo")
#ws = websocket("ws://localhost:9998/racer")
ws = websocket("ws://arrowtheory.com:9998/Racer3/Racer.py")
#ws = websocket("ws://localhost:9998/Racer3/Racer.py")

def onopen():
    #ws.send("hi hi hi!")
    put_debug("Connection established")
    element = document.getElementById('messages')
    element.innerHTML = ''
    element.style.backgroundColor = "white"
    text = document.getElementById("entry_text")
    text.focus()


ws.onopen = onopen
                
def onmessage(evt):
    put_debug("Message is received:")
    data = evt.data
    put_debug(repr(data))

    if data.strip() == "CLEAR" :
        clear_message()
    elif data.strip() == "CLOSE" :
        #onclose()
        ws.close()
    else:
        put_message(evt.data)

ws.onmessage = onmessage

def onclose():
    put_debug("lost socket connection")
    put_message("<br>Lost connection. Try again later.")
    element = document.getElementById('messages')
    element.style.backgroundColor = "pink"

ws.onclose = onclose


def onclick():
    put_debug("sending:")
    put_debug(text.value)
    ws.send(text.value)
    text.value = ""

button = document.getElementById("entry_button")
text = document.getElementById("entry_text")
#button.onclick = onclick

def onkeydown(evt):
    if evt.keyCode==13:
        onclick()

text.onkeydown = onkeydown



                
