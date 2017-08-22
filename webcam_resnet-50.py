
# -*- coding: utf-8 -*-
# /home/victoria/projects/computer_vision/keras_js_canvas/webcam_resnet-50.py

# ----------------------------------------------------------------------------
# EXECUTE SCRIPT IN PYTHON 2.7 VENV (HAS REQUIRED, INSTALLED OPENCV, IMUTILS, CAFFE ... PACKAGES):
import os

# FIRST, SEE IF WE ARE IN A CONDA VENV { py27: PYTHON 2.7 | py35: PYTHON 3.5 | tf: TENSORFLOW | thee : THEANO }
try:
    os.environ["CONDA_DEFAULT_ENV"]
except KeyError:

    print("\n\tPlease set the py27 { p2 | Python 2.7 } environment!\n")
    exit()

# IF WE ARE IN A CONDA VENV, REQUIRE THE p2 VENV:
if os.environ['CONDA_DEFAULT_ENV'] != "py27":
    print("\n\tPlease set the py27 { p2 | Python 2.7 } environment!\n")
    exit()
# more here: file:///home/victoria/projects/reference/Python%20Notes.html#Environments
# ----------------------------------------------------------------------------

# ============================================================================
# for some reason this must appear here ...

def preprocess_input(x):
    x /= 255.
    x -= 0.5
    x *= 2.
    return x

# ... or get:
#
#     ('\n\tPredicted:', [(u'n01930112', u'nematode', 0.15050603), (u'n03207941', u'dishwasher', 0.024237579), (u'n03729826', u'matchstick', 0.02144454)], '\n')

# ============================================================================

print("\n\tHello Victoria!\n")

# ----------------------------------------------------------------------------
# https://keras.io/applications/

from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

model = ResNet50(weights='imagenet')

#img_path = 'images/elephant.jpg'
##img_path = 'images/frame.jpg'
##img_path = 'images/yellowstone-wolf.jpg'

#img = image.load_img(img_path, target_size=(224, 224))
#x = image.img_to_array(img)
#x = np.expand_dims(x, axis=0)
#x = preprocess_input(x)

#preds = model.predict(x)
## decode the results into a list of tuples (class, description, probability)
## (one such list for each sample in the batch)
#print('\n\tPredicted:', decode_predictions(preds, top=3)[0], '\n')
## Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]

# ----------------------------------------------------------------------------

#processing = False

# ----------------------------------------------------------------------------
# /mnt/Vancouver/apps/openface/demos/classifier_webcam.py

import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument(
        '--captureDevice',
        type=int,
        #default=0,
        default=-1,     ## see docstring, above!
        #default=1,     ## << Victoria: tried this: threw error:  "VIDEOIO ERROR: V4L: index 1 is not correct!"
        help='Capture device. 0 for latop webcam and 1 for usb webcam')    ## ... as this may? actually be the reverse?
parser.add_argument('--width', type=int, default=320)
parser.add_argument('--height', type=int, default=240)
#parser.add_argument('--width', type=int, default=512)
#parser.add_argument('--height', type=int, default=288)
#parser.add_argument('--width', type=int, default=229)       ## 229 for inception v3
#parser.add_argument('--height', type=int, default=229)

args = parser.parse_args()

video_capture = cv2.VideoCapture(args.captureDevice)
video_capture.set(3, args.width)
video_capture.set(4, args.height)
#video_capture.set(3, 320)
#video_capture.set(4, 240)

#while True:
    #ret, frame = video_capture.read()
    ##cv2.imshow('', frame)

    ## ----------------------------------------
    ##preds = model.predict(ret, frame)
    ### decode the results into a list of tuples (class, description, probability)
    ### (one such list for each sample in the batch)
    ##print('\n\tPredicted:', decode_predictions(preds, top=3)[0], '\n')
    ### Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]
    ## ----------------------------------------

    #cv2.imshow('Victoria - test', frame)
    ## quit the program on the press of key 'q' :
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break
## When everything is done, release the capture
#video_capture.release()
#cv2.destroyAllWindows()

# ----------------------------------------------------------------------------
# http://stackoverflow.com/questions/18954889/how-to-process-images-of-a-video-frame-by-frame-in-video-streaming-using-opencv

#import time
#start = time.time()

#video_capture = cv2.VideoCapture('path of video file')
#video_capture = cv2.VideoCapture(args.captureDevice)
#count = 0


# ----------------------------------------------------------------------------
#html - How to update an existing Python Flask web page based on form input? - Stack Overflow
#http://stackoverflow.com/questions/38641484/how-to-update-an-existing-python-flask-web-page-based-on-form-input
## ------------------
#Welcome | Flask (A Python Microframework)
#http://flask.pocoo.org/
## ------------------
#Using Flask for Scientific Web Applications
#http://hplgit.github.io/web4sciapps/doc/pub/._web4sa_flask013.html
## ------------------
#Converting a simple website to Python Flask | Vert Studios
#http://vertstudios.com/blog/new-flask-site/
## ------------------
#Worksheet - Build a Python Web Server with Flask | Raspberry Pi Learning Resources
#https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/
#HTTP streaming of command output in Python Flask | Musing Mortoray
#https://mortoray.com/2014/03/04/http-streaming-of-command-output-in-python-flask/
## ------------------
#
#from flask import Flask
#app = Flask(__name__)
#
###@app.route("/")
###def hello():
    ###return "Hello World!"
#@app.route("/webcam_canvas_test1.html")
def webcam_nn():
    # http://stackoverflow.com/questions/25023233/how-to-save-python-screen-output-to-a-text-file
    # http://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w
    #f = open('webcam.out', 'w+')        ## w+ : opens a file for both writing and reading. Overwrites the existing file if the
                                        ##  file exists. If the file does not exist, creates a new file for reading and writing.
    while video_capture.isOpened():
    #while True:
        ret,frame = video_capture.read()
        # SHOW THE VIDEO STREAM:
        cv2.imshow('Logitech C270 webcam', frame)
        #cv2.imwrite("frame%d.jpg" % count, frame)
        #count += 1
        ###image = video_capture.read()[1]

        #if count %25 == 0:                           ## http://stackoverflow.com/questions/28224280/how-to-process-video-files-with-python-opencv-faster-than-file-frame-rate
        #if count == 10 or count %100 == 0:           ## http://stackoverflow.com/questions/28224280/how-to-process-video-files-with-python-opencv-faster-than-file-frame-rate
        #if count == 10 or count %10 == 0:            ## http://stackoverflow.com/questions/28224280/how-to-process-video-files-with-python-opencv-faster-than-file-frame-rate
        #if count == 10 or count %1 == 0:             ## http://stackoverflow.com/questions/28224280/how-to-process-video-files-with-python-opencv-faster-than-file-frame-rate
        # ----------------------------------------------------------------------------
        # THIS SUBSECTION WAS INDENTED UNDER THE IF LOOP, ABOVE
        #print("time", time.time() - start)
        #print(image)
        #frame = np.array(frame)
        #resized_frame = cv2.resize(frame, (480, 360), interpolation = cv2.INTER_AREA)
        resized_frame = cv2.resize(frame, (360, 280), interpolation = cv2.INTER_AREA)
        # WRITE FRAME TO IKAGE:
        cv2.imwrite("out/frame.jpg", resized_frame)
        #img_path = 'images/elephant.jpg'
        #img_path = 'images/yellowstone-wolf.jpg'
        img_path = 'out/frame.jpg'
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = model.predict(x)
        #print
        #print("Predicted:", decode_predictions(preds, top=5)[0])
        #print(decode_predictions(preds, top=5)[0])
        # ----------------------------------------
        # http://stackoverflow.com/questions/19112735/python-print-tuple-elements-with-no-brackets
        # http://stackoverflow.com/questions/27071745/overwriting-a-file-in-python
        with open('out/webcam.csv', 'w') as f:
            for item in decode_predictions(preds, top=5)[0]:
                print(str(item[1]) + ': ' + str(item[2]))
                f.write(str(item[1]) + ',' + str(item[2]) + '\n')       ## outputs CSV file, overwrites at each iteration (for canvas.js dynamic bar plot)
        # ----------------------------------------
        ## http://stackoverflow.com/questions/19112735/python-print-tuple-elements-with-no-brackets
        #for item in decode_predictions(preds, top=5)[0]:
            #print(str(item[1]) + ': ' + str(item[2]))
            ## http://stackoverflow.com/questions/27071745/overwriting-a-file-in-python
            #with open('webcam.out', 'w') as f:
                #f.write(str(item[1]) + ',' + str(item[2]) + '\n')       ## outputs CSV file, overwrites at each iteration (for canvas.js dynamic bar plot)
                ##f.write("---------------\n")                           ## for debugging
            ##f.write('[\"' + str(item[1]) + '\", ' + str(item[2]) + ']\n')
        # COMMENT F.WRITE() LINE ABOVE AND UNCOMMENT FOLLOWING LINES, TO GET ALL DATA OUTPUTTED
        ### SWITCH TO THIS:
        ### f = open('webcam.out', 'w+')
        #print("---------------")
        #f.write("---------------\n")
        # ----------------------------------------
        #return "Predicted:", decode_predictions(preds, top=3)[0]
        #return "Hello World!"
        #return "Predicted:", decode_predictions(preds, top=3)[0]
        # END OF PREVIOUSLY INDENTED SUBSECTION
        # ----------------------------------------------------------------------------
        if cv2.waitKey(10) & 0xFF == ord('q'):
            f.close()
            break

    video_capture.release()
    cv2.destroyAllWindows()
    video_capture.release()

if __name__ == "__main__":
    #app.run()
    webcam_nn()


"""(py27) [victoria@victoria keras]$ python webcam.py

        Hello Victoria!

    Using Theano backend.
    (Subtensor{int64}.0, Elemwise{add,no_inplace}.0, Elemwise{add,no_inplace}.0, Subtensor{int64}.0)
    libv4l2: error setting pixformat: Device or resource busy
    ...
    libv4l2: error setting pixformat: Device or resource busy
    VIDEOIO ERROR: V4L2: Pixel format of incoming image is unsupported by OpenCV

(py27) [victoria@victoria keras]$ wcrs

  [resetting USB webcam]
[sudo] password for victoria:

resetting USB (Logitech C270) webcam ...
Resetting USB device /dev/bus/usb/001/079
Reset successful
done!

(py27) [victoria@victoria keras]$ python webcam.py

        Hello Victoria!

    Using Theano backend.
    (Subtensor{int64}.0, Elemwise{add,no_inplace}.0, Elemwise{add,no_inplace}.0, Subtensor{int64}.0)
    ...
"""
# ============================================================================
