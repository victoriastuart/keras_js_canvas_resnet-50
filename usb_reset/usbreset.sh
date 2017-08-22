#!/bin/bash

# /mnt/Vancouver/Programming/scripts/usb_reset/usbreset.sh

# reset Logitech C270 USB webcam

# notes: see /mnt/Vancouver/Programming/scripts/usb_reset/_README - Victoria.txt

# ~/.bashrc aliases: usbreset | usbrs | wcrs

# USAGE:

mouse=$( lsusb | grep -i logitech | perl -nE "/\D+(\d+)\D+(\d+).+/; print qq(\$1/\$2)")

echo
echo 'resetting USB (Logitech C270) webcam ...'

/mnt/Vancouver/Programming/scripts/usb_reset/usbreset  /dev/bus/usb/$mouse

sleep 5
echo 'done!'
echo
