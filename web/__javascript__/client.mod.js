	(function () {
		var status = function (message) {
			document.getElementById ('messages').innerHTML = message;
		};
		var put_debug = function () {
			var info = tuple ([].slice.apply (arguments).slice (0));
			var element = document.getElementById ('debug');
		};
		var do_debug = function () {
			var info = tuple ([].slice.apply (arguments).slice (0));
			var element = document.getElementById ('debug');
			element.innerHTML += ' '.join (function () {
				var __accu0__ = [];
				var __iterable0__ = info;
				for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
					var i = __iterable0__ [__index0__];
					__accu0__.append (str (i) + '<br>');
				}
				return __accu0__;
			} ());
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
		var str_index = function (data, match) {
			var idx = 0;
			var n = len (match);
			while (idx + n <= len (data)) {
				if (data.__getslice__ (idx, idx + n, 1) == match) {
					return idx;
				}
				idx++;
			}
			return null;
		};
		var get_params = function () {
			var href = window.location.href;
			var idx = str_index (href, '?');
			if (idx === null) {
				return dict ({});
			}
			var params = href.__getslice__ (idx + 1, null, 1);
			var idx = str_index (params, '=');
			var arg = params.__getslice__ (0, idx, 1);
			var value = params.__getslice__ (idx + 1, null, 1);
			var data = dict ([[arg, value]]);
			return data;
		};
		var host = window.location.hostname;
		if (len (host) == 0) {
			var host = 'localhost';
		}
		var params = get_params ();
		var game = params.py_get ('game');
		var game = game.py_replace ('%2F', '/');
		var addr = 'ws://{}:9998/{}'.format (host, game);
		var ws = websocket (addr);
		var onopen = function () {
			put_debug ('Connection established');
			var element = document.getElementById ('messages');
			element.innerHTML = '';
			element.style.backgroundColor = 'white';
			var text = document.getElementById ('entry_text');
			text.focus ();
		};
		ws.onopen = onopen;
		var CLEAR = 'SHAKESPY_CLEAR\n';
		var CLOSE = 'SHAKESPY_CLOSE\n';
		var onmessage = function (evt) {
			put_debug ('Message is received:');
			var data = evt.data;
			put_debug (repr (data));
			if (__in__ (CLOSE, data)) {
				ws.close ();
				return ;
			}
			if (__in__ (CLEAR, data)) {
				clear_message ();
				var idx = str_index (data, CLEAR);
				var data = data.__getslice__ (0, idx, 1) + data.__getslice__ (idx + len (CLEAR), null, 1);
			}
			put_message (data);
			window.scrollBy (0, 100);
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
			__all__.CLEAR = CLEAR;
			__all__.CLOSE = CLOSE;
			__all__.addr = addr;
			__all__.button = button;
			__all__.clear_message = clear_message;
			__all__.do_debug = do_debug;
			__all__.element = element;
			__all__.game = game;
			__all__.get_params = get_params;
			__all__.host = host;
			__all__.message_data = message_data;
			__all__.onclick = onclick;
			__all__.onclose = onclose;
			__all__.onkeydown = onkeydown;
			__all__.onmessage = onmessage;
			__all__.onopen = onopen;
			__all__.params = params;
			__all__.put_debug = put_debug;
			__all__.put_message = put_message;
			__all__.status = status;
			__all__.str_index = str_index;
			__all__.text = text;
			__all__.ws = ws;
		__pragma__ ('</all>')
	}) ();
