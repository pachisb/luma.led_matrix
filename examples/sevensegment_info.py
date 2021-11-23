#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Example for seven segment displays.
"""

import time
from datetime import datetime
import subprocess

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment


def date(seg):
    """
    Display current date on device.
    """
    now = datetime.now()
    seg.text = now.strftime("%y-%m-%d")


def clock(seg, seconds):
    """
    Display current time on device.
    """
    interval = 0.5
    for i in range(int(seconds / interval)):
        now = datetime.now()
        seg.text = now.strftime("%H-%M-%S")

        # calculate blinking dot
        if i % 2 == 0:
            seg.text = now.strftime("%H-%M-%S")
        else:
            seg.text = now.strftime("%H %M %S")

        time.sleep(interval)


def show_message_vp(device, msg, delay=0.1):
    # Implemented with virtual viewport
    width = device.width
    padding = " " * width
    msg = padding + msg + padding
    n = len(msg)

    virtual = viewport(device, width=n, height=8)
    sevensegment(virtual).text = msg
    for i in reversed(list(range(n - width))):
        virtual.set_position((i, 0))
        time.sleep(delay)


def show_message_alt(seg, msg, delay=0.1):
    # Does same as above but does string slicing itself
    width = seg.device.width
    padding = " " * width
    msg = padding + msg + padding

    for i in range(len(msg)):
        seg.text = msg[i:i + width]
        time.sleep(delay)


def main():
    # Create seven segment device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1)
    seg = sevensegment(device)

    # Get IP info
    command = 'ip a show up | grep "    inet " | grep -v -e inet6 -e 127.0.0 | sed "s/\/.*//" | sed "s/inet//" | tr -s "\\n " " " | tr "." "-"'

    # Brightness
    for intensity in range(16):
        seg.device.contrast(intensity * 16)
        seg.text = "HELLO PI"
        time.sleep(0.2)
    device.contrast(0x7F)

    # Info display loop
    while True:
        date(seg)
        time.sleep(2)
        clock(seg, seconds=2)
        process = subprocess.run(['sh', '-c', command], check=False, stdout=subprocess.PIPE, universal_newlines=True)
        output = process.stdout.strip()
        show_message_vp(device, "IP " + output, delay=0.25)
        time.sleep(2)
        show_message_vp(device, "IP " + output, delay=0.25)


if __name__ == '__main__':
    main()
