
# -*- coding: utf-8 -*-
# /home/victoria/projects/computer_vision/keras_js_canvas/webcam_cv2_basic.py

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

import cv2

video_capture = cv2.VideoCapture(-1)
video_capture.set(3, 320)
video_capture.set(4, 240)
while video_capture.isOpened():
    ret,frame = video_capture.read()
    cv2.imshow('window-name', frame)

    resized_frame = cv2.resize(frame, (480, 360), interpolation = cv2.INTER_AREA)
    cv2.imwrite("out/frame.jpg", resized_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):      ## << need this, too!
        break

video_capture.release()
cv2.destroyAllWindows()
video_capture.release()

# ============================================================================
