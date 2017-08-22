
==============================================================================
/mnt/Vancouver/Programming/scripts/usb_reset/_README - Victoria.txt

2016-Dec-21
==============================================================================

How do you reset a USB device from the command line? - Ask Ubuntu
https://askubuntu.com/questions/645/how-do-you-reset-a-usb-device-from-the-command-line/661#661

A1. [up vote 66; accepted]  Save the following as usbreset.c

/* usbreset -- send a USB port reset to a USB device */

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/ioctl.h>

#include <linux/usbdevice_fs.h>


int main(int argc, char **argv)
{
    const char *filename;
    int fd;
    int rc;

    if (argc != 2) {
        fprintf(stderr, "Usage: usbreset device-filename\n");
        return 1;
    }
    filename = argv[1];

    fd = open(filename, O_WRONLY);
    if (fd < 0) {
        perror("Error opening output file");
        return 1;
    }

    printf("Resetting USB device %s\n", filename);
    rc = ioctl(fd, USBDEVFS_RESET, 0);
    if (rc < 0) {
        perror("Error in ioctl");
        return 1;
    }
    printf("Reset successful\n");

    close(fd);
    return 0;
}

The run the following commands in terminal:

    Compile the program:

    $ cc usbreset.c -o usbreset

    Get the Bus and Device ID of the USB device you want to reset:

    $ lsusb
    Bus 002 Device 003: ID 0fe9:9010 DVICO

    Make our compiled program executable:

    $ chmod +x usbreset

    Execute the program with sudo privilege; make necessary substitution for <Bus> and <Device> ids as found by running the lsusb command:

    $ sudo ./usbreset /dev/bus/usb/002/003

Source of above program: http://marc.info/?l=linux-usb&m=121459435621262&w=2

> This works with ubuntu 13.10. The device ID can vary. TO get it for the mouse I have wrapped above code in few shell commands:

    echo $(lsusb | grep Mouse) mouse=$( lsusb | grep Mouse | perl -nE "/\D+(\d+)\D+(\d+).+/; print qq(\$1/\$2)") sudo /path/to/c-program/usbreset /dev/bus/usb/$mouse

=============================================================================

[victoria@victoria usb_reset]$ date
    Wed Dec 21 09:26:02 PST 2016
[victoria@victoria usb_reset]$ pwd
    /mnt/Vancouver/Programming/scripts/usb_reset

[victoria@victoria usb_reset]$ cc usbreset.c -o usbreset

[victoria@victoria usb_reset]$ l

    total 328K
    drwxr-xr-x 2 victoria victoria 4.0K Dec 21 09:20 'How do you reset a USB device from the command line? - Ask Ubuntu_files'
    -rw-r--r-- 1 victoria victoria 308K Dec 21 09:20 'How do you reset a USB device from the command line? - Ask Ubuntu.htm'
    -rwxr-xr-x 1 victoria victoria 8.6K Dec 21 09:20  usbreset
    -rw-r--r-- 1 victoria victoria  764 Dec 21 09:20  usbreset.c

[victoria@victoria usb_reset]$ lsusb | grep -i logitech
    Bus 001 Device 057: ID 046d:0825 Logitech, Inc. Webcam C270

[victoria@victoria usb_reset]$ echo $(lsusb | grep -i logitech) mouse=$( lsusb | grep -i logitech | perl -nE "/\D+(\d+)\D+(\d+).+/; print qq(\$1/\$2)")
    Bus 001 Device 057: ID 046d:0825 Logitech, Inc. Webcam C270 mouse=001/057

[victoria@victoria usb_reset]$ mouse=$( lsusb | grep -i logitech | perl -nE "/\D+(\d+)\D+(\d+).+/; print qq(\$1/\$2)")

[victoria@victoria usb_reset]$ echo $mouse
    001/057

[victoria@victoria usb_reset]$

==============================================================================

Reset USB (Logitech C270) webcam:
---------------------------------

* Script:

    /mnt/Vancouver/Programming/scripts/usb_reset/usbreset.sh

... calls binary executable

    /mnt/Vancouver/Programming/scripts/usb_reset/usbreset

* ~/.bashrc aliases: usbreset | usbrs | wcrs

* Notes:

    /mnt/Vancouver/Programming/scripts/usb_reset/usbreset.sh
    /mnt/Vancouver/Programming/scripts/usb_reset/_README - Victoria.txt

==============================================================================

