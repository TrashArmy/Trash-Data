'''
    File name: main.py
    Author: Sagar Mandal, Stephen Brotman, Charith Dassanayake, Sahithi Bonala, Brandon Sheu
    Date created: 1/29/2018
    Date last modified: 1/30/2018
    Python Version: 2.7
'''

import picamera
import os
from time import sleep, gmtime, strftime
from light import lightOn, lightOff

from keypress import getch
CONST_DATADIR = "./images/"


def validateDir(name):
    if not os.path.exists(name):
        return name
    else:
        i = 1
        temp = name
        while i < 200 and os.path.exists(name):
            name = temp + "_" + str(i);
            i += 1
        if i == 200:
            raise Exception("Name value exceeding limit")
        return name

def getCreateDir(name):
    name = CONST_DATADIR + name;
    name = validateDir(name)
    os.makedirs(name)
    return name

def getFolderName():
    return strftime("%Y%m%d", gmtime())
    
if __name__ == "__main__":
    camera = picamera.PiCamera()
    camera.resolution = (1024, 1024)
    button_delay = 0.2
    dir_name = getCreateDir(getFolderName())
    i = 1
    while True:
        char = getch()        
        if (char == "p"):
            print("Stop!")
            break     
        if (char == "q"):
            file_name = dir_name + "/" + str(i) + ".jpg"
            lightOn()
            camera.capture(file_name, resize = (480, 480))
            print("Captured Image: " + str(i) + ".jpg")
            lightOff()
            os.system("xdg-open " + file_name)
            i += 1
    lightOff()
    print("Terminating Program")
            
        