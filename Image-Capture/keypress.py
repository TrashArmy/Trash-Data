#!/usr/bin/python3
 
# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
 
import sys
from tty import setraw
from termios import TCSADRAIN, tcsetattr, tcgetattr 
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = tcgetattr(fd)
    try:
        setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        tcsetattr(fd, TCSADRAIN, old_settings)
    return ch