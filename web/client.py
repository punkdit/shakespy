

def status(message):
    document.getElementById('messages').innerHTML = message


def put_debug(*info):
    element = document.getElementById('debug')
    #element.innerHTML += ' '.join([str(i)+"<br>" for i in info]) #+ "<br>"

def do_debug(*info):
    element = document.getElementById('debug')
    element.innerHTML += ' '.join([str(i)+"<br>" for i in info]) #+ "<br>"


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
element.style.backgroundColor = "lightgrey" # waiting to connect


def str_index(data, match):
    idx = 0
    n = len(match)
    while idx+n <= len(data):
        if data[idx : idx+n] == match:
            return idx
        idx += 1
    return None


def get_params():
    href = window.location.href
    #do_debug(href)
    idx = str_index(href, "?")
    if idx is None:
        return {}
    params = href[idx+1:]
    #do_debug(params)
    idx = str_index(params, "=")
    arg = params[:idx]
    value = params[idx+1:]
    data = {arg : value}
    #do_debug(data)
    return data

                
host = window.location.hostname
if len(host)==0:
    host = "localhost"
#do_debug("host", len(host), "thats it")

params = get_params()
game = params.get("game")
game = game.replace("%2F", "/")
#do_debug("here:", game)

addr = "ws://{}:9998/{}".format(host, game)
ws = websocket(addr)


def onopen():
    #ws.send("hi hi hi!")
    put_debug("Connection established")
    element = document.getElementById('messages')
    element.innerHTML = ''
    element.style.backgroundColor = "white"
    text = document.getElementById("entry_text")
    text.focus()


ws.onopen = onopen

CLEAR = "SHAKESPY_CLEAR\n"
CLOSE = "SHAKESPY_CLOSE\n"

def onmessage(evt):
    put_debug("Message is received:")
    data = evt.data
    put_debug(repr(data))

    if CLOSE in data:
        #do_debug(CLOSE)
        ws.close()
        return

    if CLEAR in data:
        #do_debug(CLEAR)
        clear_message()
        #idx = data.index(CLEAR) # transcrypt FAIL
        idx = str_index(data, CLEAR)
        data = data[:idx] + data[idx + len(CLEAR):]

    put_message(data)

    #window.scrollTo(0, 0)
    window.scrollBy(0, 100)


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



                
