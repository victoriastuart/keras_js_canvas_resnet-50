# keras_js_canvas_resnet-50
Resnet-50 image classifier in web browser

Abbreviated notes, here: see the webpage HTML code for webpage-related notes, and the python script for additional comments. Briefly, however:

Dependencies:

* Python 2.7 (venv)
* Keras
* OpenCV (for "cv2")
* Theano
* Numpy

Usage:

* run the script, ```webcam_resnet-50.py```
* load webserver (notes below)
* open webpage, ```webcam_resnet-50.html```

Web pages:

* webcam_resnet-50.html : draft version, fully commented including debugging statements
* webcam_resnet-50-brief.html : fewer comments; easier to read, otherwise identical HTML code

Webserver:

At the time I believe just used a node (node.js)-installed server that I had previously installed for CaffeJS,

    /mnt/Vancouver/apps/caffejs/node_modules/.bin/http-server -p 5000

However, you can just install (node) a global copy,

    [sudo] npm install http-server -g       ## -g : install globally (avail any dir, venv)

that you can spin up as needed:

    (py27) [victoria@victoria ~]$ http-server

        Starting up http-server, serving ./
        Available on:
          http://127.0.0.1:8080
          http://192.168.1.4:8080
        Hit CTRL-C to stop the server

Or, you can simply run any of these in terminal:

    http-server                     ## installed, globally, via NPM (notes below)
    python2 -m SimpleHTTPServer     ## Python 2
    python -m http.server 5000      ## Python 3

and navigate to localhost:port, e.g.:

    http://localhost:8000/
    http://127.0.0.1:8000/
    --------------------
    http://0.0.0.0:8000/            ## the web app will be accessible to any device on the network
    http://192.168.1.4:8000/
    http://10.24.10.6:8000/


regarding the latter, I am typing this ~ 8 months since I last looked at that code, so the ports may/may not work ...  If it's an issue, try ports

    5000
    8000
    8080

