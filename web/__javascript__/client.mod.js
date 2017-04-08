	(function () {
		var status = function (message) {
			document.getElementById ('messages').innerHTML = message;
		};
		var put_debug = function () {
			var info = tuple ([].slice.apply (arguments).slice (0));
			var element = document.getElementById ('debug');
		};
		var message_data = '';
		var put_message = function () {
			var info = tuple ([].slice.apply (arguments).slice (0));
			message_data += ' '.join (function () {
				var __accu0__ = [];
				var __iterable0__ = info;
				for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
					var i = __iterable0__ [__index0__];
					__accu0__.append (str (i));
				}
				return __accu0__;
			} ());
			var element = document.getElementById ('messages');
			element.innerHTML = '<pre>{}</pre>'.format (message_data);
		};
		var clear_message = function () {
			put_debug ('clear_message');
			var element = document.getElementById ('messages');
			element.innerHTML = '';
			message_data = '';
		};
		var element = document.getElementById ('messages');
		element.style.backgroundColor = 'lightgrey';
		var ws = websocket ('ws://arrowtheory.com:9998/Racer3/Racer.py');
		var onopen = function () {
			put_debug ('Connection established');
			var element = document.getElementById ('messages');
			element.innerHTML = '';
			element.style.backgroundColor = 'white';
			var text = document.getElementById ('entry_text');
			text.focus ();
		};
		ws.onopen = onopen;
		var onmessage = function (evt) {
			put_debug ('Message is received:');
			var data = evt.data;
			put_debug (repr (data));
			if (data.strip () == 'CLEAR') {
				clear_message ();
			}
			else if (data.strip () == 'CLOSE') {
				ws.close ();
			}
			else {
				put_message (evt.data);
			}
		};
		ws.onmessage = onmessage;
		var onclose = function () {
			put_debug ('lost socket connection');
			put_message ('<br>Lost connection. Try again later.');
			var element = document.getElementById ('messages');
			element.style.backgroundColor = 'pink';
		};
		ws.onclose = onclose;
		var onclick = function () {
			put_debug ('sending:');
			put_debug (text.value);
			ws.send (text.value);
			text.value = '';
		};
		var button = document.getElementById ('entry_button');
		var text = document.getElementById ('entry_text');
		var onkeydown = function (evt) {
			if (evt.keyCode == 13) {
				onclick ();
			}
		};
		text.onkeydown = onkeydown;
		__pragma__ ('<all>')
			__all__.button = button;
			__all__.clear_message = clear_message;
			__all__.element = element;
			__all__.message_data = message_data;
			__all__.onclick = onclick;
			__all__.onclose = onclose;
			__all__.onkeydown = onkeydown;
			__all__.onmessage = onmessage;
			__all__.onopen = onopen;
			__all__.put_debug = put_debug;
			__all__.put_message = put_message;
			__all__.status = status;
			__all__.text = text;
			__all__.ws = ws;
		__pragma__ ('</all>')
	}) ();
