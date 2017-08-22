
==============================================================================
README: webcam_resnet-50

/home/victoria/projects/computer_vision/keras_js_canvas/_readme (webcam_resnet-50) Victoria.txt
==============================================================================

* See also draft notes,

    /home/victoria/projects/computer_vision/keras_js_canvas/drafts/webcam neural net classification -  draft notes.txt


==============================================================================
WEBCAM_RESNET-50 [KERAS-JS | RESNET-50]
=======================================

[2016-Dec-29] For the past ~2 weeks I worked on recreating (myself!) the the CaffeJS, Keras-JS, and particularly the "Machine Learning for Artists keras-js ResNet live webcam demo,"

    https://ml4a.github.io/demos/keras.js/

My code essentially recreates the latter project, via my own approach/solutions!  😀


==============================================================================
SUMMARY
=======

* NN architecture: Keras-js; Keras ResNet-50

* Implementation -- Python 2.7:

 ** OpenCV cv2 webcam capture, frame output for "video" rendering in HTML canvas

 ** ResNet-50 NN, object classification, output to CSV file

* Implementation -- HTML:

 ** webcam preview from OpenCV frame capture, rendered in HTML canvas/container

 ** visualization of ResNet-50 classifications in CanvasJS chart, rendered in HTML canvas/container

 ** JavaScript debugging, using Firefox's embedded Firefox Developer Tools  [Ctrl-Alt-I]

* Additionally:

 ** HTML: coding of multiple canvases/containers (see commented-out subsections in webcam_resnet-50.html)

 ** HTML: CORS issues when downloading CSV data over the web (JQuery security issue, 'non-resolved;' ibid.)

 ** HTML: direct display of OpenCV webcam stream in HTML page/canvas/container

 *** ... for reference only (code commented out in webcam_resnet-50.html).  Issue: cannot simultaneously use webcam in a browser and a script; hence, the need to render the webcam preview in the HTML page as a "video" rendered from captured frames (JPG images).

 ** [Aside]  Flask: While working on this project I also tried some Flask-based approaches [none ultimately implemented, thus far]; see the commented-out sections in webcam_resnet-50.py, the files in this directory, and these web pages [Google: various ...]:

* Project:

    /home/victoria/projects/computer_vision/keras_js_canvas/

* Here is the web page:

    /home/victoria/projects/computer_vision/keras_js_canvas/webcam_resnet-50.html.


==============================================================================
IMPLEMENTATION
==============

* Python 2.7 script: ~/projects/computer_vision/keras_js_canvas/webcam_resnet-50.py

* Here are some early, 'raw' draft notes.

    /home/victoria/projects/computer_vision/keras_js_canvas/drafts/webcam neural net classification -  draft notes.txt

* In frustration (re: trying to get the ChartJS bar graph to work, and also reading from local CSV files/data), I posted some questions here  [local copy;  plain-text copy]. The responses I received (especially to my inaugural post:completely unaddressed, grrrrrr....!!) were totally useless!!

I ended up solving everything myself, as summarized there!  :-/

* HTML code: webcam_resnet-50.html  [fully commented]  |  webcam_resnet-50-brief.html  [edited for brevity]


========================================
DEPENDENCIES:
=============

* Python 2.7 (venv)
* Keras
* OpenCV (for "cv2")
* Theano
* Numpy

------------------------------------------------------------------------------
THEANO:
=======

Install the latest Theano, from the GitHub repo:

    pip install git+git://github.com/Theano/Theano.git@master

----------------------------------------

victoria:$ pip uninstall theano

    DEPRECATION: Uninstalling a distutils installed project (theano) has been deprecated and will be removed in a future version. This is due to the fact that uninstalling a distutils project will only partially uninstall the project.
    Uninstalling Theano-0.7.0:
    /media/Vancouver/apps/anaconda/anaconda2/lib/python2.7/site-packages/Theano-0.7.0-py2.7.egg-info
    Proceed (y/n)? y
    Successfully uninstalled Theano-0.7.0

victoria:$ pip install git+git://github.com/Theano/Theano.git@master

    Collecting git+git://github.com/Theano/Theano.git@master
      Cloning git://github.com/Theano/Theano.git (to master) to /tmp/pip-tuV59j-build
    Requirement already satisfied (use --upgrade to upgrade): numpy>=1.7.1 in /media/Vancouver/apps/anaconda/anaconda2/lib/python2.7/site-packages (from Theano==0.7.0)
    Requirement already satisfied (use --upgrade to upgrade): scipy>=0.11 in /media/Vancouver/apps/anaconda/anaconda2/lib/python2.7/site-packages (from Theano==0.7.0)
    Requirement already satisfied (use --upgrade to upgrade): six>=1.9.0 in /media/Vancouver/apps/anaconda/anaconda2/lib/python2.7/site-packages (from Theano==0.7.0)
    Installing collected packages: Theano
      Running setup.py install for Theano
    Successfully installed Theano-0.7.0

victoria:$

------------------------------------------------------------------------------
KERAS:
======

https://github.com/fchollet/keras/issues/807

AttributeError: 'module' object has no attribute 'relu'

Keras recently updated their relu to use the Theano implementation (https://github.com/fchollet/keras/pull/732)

    pip uninstall theano
    pip install git+git://github.com/Theano/Theano.git@master

----------------------------------------

From: "Victoria Stuart (gmail)
To: "Victoria Stuart (gmail)
Keras - updating
Date: Tue, 16 Aug 2016

https://github.com/fchollet/keras/issues/3481

Check that you are up-to-date with the master branch of Keras. You can update with:

    pip install git+git://github.com/fchollet/keras.git --upgrade --no-deps

If running on Theano, check that you are up-to-date with the master branch of Theano. You can update with:

    pip install git+git://github.com/Theano/Theano.git --upgrade --no-deps


========================================
NOTES:
======

* The "unedited" (i.e. fully-commented including debugging code) HTML code

      webcam_resnet-50.html

  contains commented-out subsections for viewing the OpenCV webcam stream.

  ** Note that you cannot simultaneously share webcam device with the browser and OpenCV scripts

and the option to deploy multiple containers/HTML canvases.  Note the need to have unique variable names, etc. in each container.

* As mentioned, debug JavaScript with Firefox's embedded Firefox Developer Tools  [Ctrl-Alt-I].

* What is using/blocking my webcam?

    (py27) [victoria@victoria keras]$ python webcam.py
            Hello Victoria!
        Using Theano backend.
        (Subtensor{int64}.0, Elemwise{add,no_inplace}.0, Elemwise{add,no_inplace}.0, Subtensor{int64}.0)
        VIDEOIO ERROR: V4L2: Pixel format of incoming image is unsupported by OpenCV
        Unable to stop the stream: Device or resource busy

    (py27) [victoria@victoria keras]$ fuser /dev/video*
        /dev/video1:         18428m

    (py27) [victoria@victoria keras]$ pgrep -l 18428
    (py27) [victoria@victoria keras]$ psgrep -l 18428
        UID        PID  PPID  C STIME TTY          TIME CMD
        victoria 18428   835 37 09:46 ?        00:37:40 firefox

    (py27) [victoria@victoria keras]$

* When needed, I wrote a script, usbreset.sh (~/.bashrc alias "wcrs" : webcam reset), that resets the webcam, freeing it for use with Python/OpenCV:

    (py27) [victoria@victoria keras_js_canvas]$ wcrs
          [resetting USB webcam]
        [sudo] password for victoria:

        resetting USB (Logitech C270) webcam ...
        Resetting USB device /dev/bus/usb/001/095
        Reset successful
        done!

        (py27) [victoria@victoria keras_js_canvas]$

        # ----------------------------------------------------------------------------

        (py27) [victoria@victoria keras]$ date
            Thu Dec 29 13:28:29 PST 2016

        (py27) [victoria@victoria keras]$ pwd
            /home/victoria/projects/computer_vision/inception/keras

        (py27) [victoria@victoria keras]$ l

            total 100K
            drwxr-xr-x 3 victoria victoria 4.0K Dec 28 12:27  css
            drwxr-xr-x 2 victoria victoria 4.0K Dec 29 11:30  drafts
            drwxr-xr-x 2 victoria victoria 4.0K Dec 28 17:04  images
            -rw-r--r-- 1 victoria victoria    0 Dec 16 16:30  __init__.py
            drwxr-xr-x 4 victoria victoria 4.0K Dec 18 19:53 'In this project I basically replicated the work
                                                              (that does not work) in this folder'
            drwxr-xr-x 2 victoria victoria 4.0K Dec 28 17:07  out
            -rw-r--r-- 1 victoria victoria 1.5K Dec 28 17:12  resnet-50.py
            -rw-r--r-- 1 victoria victoria 1.5K Dec 28 17:12  resnet-50.py.2016.12.28
            -rw-r--r-- 1 victoria victoria 1.5K Dec 29 12:23  webcam_cv2_basic.py
            -rw-r--r-- 1 victoria victoria 7.7K Dec 29 11:37  webcam_resnet-50-brief.html
            -rw-r--r-- 1 victoria victoria  15K Dec 29 10:35  webcam_resnet-50.html
            -rw-r--r-- 1 victoria victoria  14K Dec 28 17:16  webcam_resnet-50.html.2016.12.28
            -rw-r--r-- 1 victoria victoria  12K Dec 28 17:12  webcam_resnet-50.py
            -rw-r--r-- 1 victoria victoria  12K Dec 28 17:12  webcam_resnet-50.py.2016.12.28

        (py27) [victoria@victoria keras]$ python webcam_resnet-50.py

                Hello Victoria!
            Using Theano backend.
            (Subtensor{int64}.0, Elemwise{add,no_inplace}.0, Elemwise{add,no_inplace}.0, Subtensor{int64}.0)

            teddy: 0.259342
            soft-coated_wheaten_terrier: 0.0277933
            Lakeland_terrier: 0.0240512
            Maltese_dog: 0.0204337
            toy_poodle: 0.0185793

            teddy: 0.27876
            soft-coated_wheaten_terrier: 0.0227351
            Lakeland_terrier: 0.0211475
            Maltese_dog: 0.0194447
            toy_poodle: 0.0172319

            teddy: 0.299134
            Lakeland_terrier: 0.0224119
            cauliflower: 0.0159318
            computer_keyboard: 0.0157673
            desk: 0.0155931

            [ "q" pressed in webcam window]

        (py27) [victoria@victoria keras]$


==============================================================================
USAGE
=====

* run the script, ```python webcam_resnet-50.py```
* load webserver (notes below)
* open webpage, ```webcam_resnet-50.html```


WEB PAGES:
==========

* webcam_resnet-50.html : draft version, fully commented including debugging statement
* webcam_resnet-50-brief.html : fewer comments; easier to read, otherwise identical HTML code


WEBSERVER:
==========

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


==============================================================================
DEMOS
=====

* See various (Kazam) MP4 video screen captures:

    /home/victoria/projects/computer_vision/keras_js_canvas/

        demos/keras-resnet50 2016-12-29 10:39:05.mp4
        demos/keras-resnet50 2016-12-29 10:43:41.mp4
        demos/keras-resnet50 2016-12-29 10:53:22.mp4
        demos/keras-resnet50 2016-12-29 10:55:44.mp4
        keras-resnet50 2016-12-29 11:42:11.mp4
        demos/keras-resnet50 neural net + computer vision code - Victoria Stuart - 2016-12-29.mp4


==============================================================================
IMPLEMENTATION NOTE
===================

Notice the clock on the webpage?  I actually use that to refresh the ChartJS/CanvasJS chart canvas, so that the chart refreshes "seamlessly."

[Similarly, the webcam frame grab canvas auto-refreshes once every 1000 ms.]

The current neural net cycle (CPU only: I don't have a GPU) is ~1-2 iterations/sec (when I get a GPU, that should jump at least an order of magnitude).

Nevertheless, keeping the chart refresh at ~1 sec. (embedded clock) keeps the output/chart from jumping around, too much!  ;-)


==============================================================================
==============================================================================
END OF FILE
==============================================================================
==============================================================================

