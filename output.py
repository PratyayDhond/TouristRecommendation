WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 959-693-507
127.0.0.1 - - [03/Feb/2025 12:18:15] "GET / HTTP/1.1" 404 -
 * Detected change in '/home/dhondpratyay/adj/geotag/dataset/output.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 959-693-507
127.0.0.1 - - [03/Feb/2025 12:18:18] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [03/Feb/2025 12:18:18] "GET / HTTP/1.1" 404 -
 * Detected change in '/home/dhondpratyay/adj/geotag/dataset/output.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 959-693-507
127.0.0.1 - - [03/Feb/2025 12:18:21] "GET /favicon.ico HTTP/1.1" 404 -
 * Detected change in '/home/dhondpratyay/adj/geotag/dataset/output.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 959-693-507
127.0.0.1 - - [03/Feb/2025 12:18:29] "GET /recommend HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1488, in __call__
    return self.wsgi_app(environ, start_response)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1466, in wsgi_app
    response = self.handle_exception(e)
               ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1463, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 872, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 870, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 855, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dhondpratyay/adj/geotag/dataset/recommendation.py", line 108, in recommend
    user_lat = float(request.args.get('lat'))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: float() argument must be a string or a real number, not 'NoneType'
 * Detected change in '/home/dhondpratyay/adj/geotag/dataset/output.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 959-693-507
127.0.0.1 - - [03/Feb/2025 12:18:31] "GET /recommend?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 200 -
127.0.0.1 - - [03/Feb/2025 12:18:31] "GET /recommend?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 -
 * Detected change in '/home/dhondpratyay/adj/geotag/dataset/output.py', reloading
 * Restarting with stat
Traceback (most recent call last):
  File "/home/dhondpratyay/adj/geotag/dataset/./_scripts/geotagToCsv.py", line 111, in <module>
    exif = image._getexif()
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/PIL/JpegImagePlugin.py", line 495, in _getexif
    return _getexif(self)
           ^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/PIL/JpegImagePlugin.py", line 519, in _getexif
    return self.getexif()._get_merged_dict()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/PIL/Image.py", line 3773, in _get_merged_dict
    merged_dict[ExifTags.IFD.GPSInfo] = self._get_ifd_dict(
                                        ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/PIL/Image.py", line 3697, in _get_ifd_dict
    return self._fixup_dict(info)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/PIL/Image.py", line 3683, in _fixup_dict
    return {k: self._fixup(v) for k, v in src_dict.items()}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen _collections_abc>", line 894, in __iter__
  File "/usr/lib/python3/dist-packages/PIL/TiffImagePlugin.py", line 571, in __getitem__
    self[tag] = handler(self, data, self.legacy_api)  # check type
    ~~~~^^^^^
  File "/usr/lib/python3/dist-packages/PIL/TiffImagePlugin.py", line 581, in __setitem__
    self._setitem(tag, value, self.legacy_api)
  File "/usr/lib/python3/dist-packages/PIL/TiffImagePlugin.py", line 628, in _setitem
    values = tuple(info.cvt_enum(value) for value in values)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/PIL/TiffImagePlugin.py", line 628, in <genexpr>
    values = tuple(info.cvt_enum(value) for value in values)

KeyboardInterrupt
Traceback (most recent call last):
  File "/home/dhondpratyay/adj/geotag/dataset/recommendation.py", line 25, in <module>
    subprocess.run(["python3", script_path], input=dataset_dir, text=True)
  File "/usr/lib/python3.12/subprocess.py", line 550, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/subprocess.py", line 1201, in communicate
    self.wait()
  File "/usr/lib/python3.12/subprocess.py", line 1264, in wait
    return self._wait(timeout=timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/subprocess.py", line 2053, in _wait
    (pid, sts) = self._try_wait(0)
                 ^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/subprocess.py", line 2011, in _try_wait
    (pid, sts) = os.waitpid(self.pid, wait_flags)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
