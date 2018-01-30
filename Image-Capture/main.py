'''
    File name: main.py
    Author: Sagar Mandal
    Date created: 1/29/2018
    Date last modified: 1/29/2018
    Python Version: 3.6
'''

import picamera
import os
from time import sleep


def getCreateDir(name):
    if os.path.exists(name):
        raise Exception("Directory Present")
    os.makedirs(name)
    return name

def validateDir(name):
    if not os.path.exists(name):
        return name
    else:
        i = 1
        temp = name
        while i < 200 and os.path.exists(name):
            name = temp + "_" + i;
            i += 1
        if i == 200:
            raise Exception("Name value exceeding limit")
        return name
    
if __name__ == "__main__":
    camera = picamera.PiCamera()
    camera.resolution = (1024, 1024)
    i = 1
    while (1):
        x = str(input("enter input:"))
        print (x)