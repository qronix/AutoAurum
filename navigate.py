import findImg as fim
import random
import time
import clientBounds as cb
import utils
import pyautogui
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key
import _pickle as cPickle
import threading
import HumanMouse as hm



def posCamToCompass(compassName):
    utils.findClientBounds()
    # top left x , top left y, width of the area, height of the area
    # region=(cb.clientBounds["topLeft"][0],cb.clientBounds["topLeft"][1],cb.clientBounds["bottomRight"][0]-cb.clientBounds["bottomLeft"][0],cb.clientBounds["bottomRight"][1]-cb.clientBounds["topLeft"][1])
    region = {
        "topLeftX":cb.mapBounds["bottomLeft"][0],
        "topLeftY":cb.mapBounds["topLeft"][1],
        "width":(cb.clientBounds["bottomRight"][0]-cb.mapBounds["bottomLeft"][0]),
        "height":(cb.clientBounds["topRight"][1]-cb.mapBounds["bottomLeft"][1])
    }

    if cb.mapBounds != {}:
        target = fim.getImgCoords('compassTest',region)
    while target == None:
        print('finding image')

def on_click(x,y,button,pressed):
    global previousTime
    # cb.clientBounds["bottomRight"][0]-cb.clientBounds["topLeft"][0],cb.clientBounds["bottomRight"][1]-cb.clientBounds["topLeft"][1]
    if not pressed:
        print('Recording is {0}'.format(recording))
        print('Raw mouse target: {0}, {1}'.format(x,y))
        print('Client width: {0}'.format(cb.clientBounds["bottomRight"][0]-cb.clientBounds["topLeft"][0]))
        print('Client height: {0}'.format(cb.clientBounds["bottomRight"][1]-cb.clientBounds["topLeft"][1]))
        print('Client centerX: {0}'.format(cb.clientBounds["centerX"]))
        print('Client centerY: {0}'.format(cb.clientBounds["centerY"]))
        print('TargetX from centerX: {0}'.format(cb.clientBounds["centerX"]-x))
        print('TargetX from centerY: {0}'.format(cb.clientBounds["centerY"]-y))
        # pyautogui.moveTo(cb.clientBounds["centerX"],cb.clientBounds["centerY"])
        # print('Target')
        if(recording):
            prevTime = getPrevTime()
            travelDelay = time.time() - prevTime
            previousTime = time.time()
            print('timedelay is {0}'.format(travelDelay))
            step = {
                "x":cb.clientBounds["centerX"]-x,
                "y":cb.clientBounds["centerY"]-y,
                "waitTime": travelDelay
            }
            path.append(step)
            print('Path: {0}'.format(path))
            # travelTime = time.time()
    else:
        pass
def getPrevTime():
    return previousTime
def on_press(key):
    global recording
    if key == Key.backspace:
        recording = True
        print('Recording')
        print(recording)
    if key == Key.end:
        recording = False
        print('Stopped recording')
        writePathToFile()

def setupNavigation():
    utils.findClientBounds()
    pyautogui.moveTo(cb.clientBounds["centerX"],cb.clientBounds["centerY"])
    target = {
        "clientBounds":cb.clientBounds,
        "compassStartDeg":0,
        "start":'geEntrance',
        "target":'geBanker'
    }
    path.append(target)

    with mouse.Listener(on_click=on_click) as listener:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

def writePathToFile():
    global path
    fileName = '{0}_to_{1}.p'.format(path[0]["start"],path[0]["target"])
    cPickle.dump(path,open(fileName,"wb"))
    print('Path written to file')
    path = []

def readPathFile():
    global path
    path = cPickle.load(open("geEntrance_to_geBanker.p","rb"))
    print('Loaded path as {0}'.format(path))
    print('Path starts at: {0}'.format(path[0]["start"]))
    navigatePath()

def navigatePath():
    if path != []:
        print('Navigating path....')
        pathInfo = path[0]
        print(pathInfo)
        del path[0]
        for step in path:
            cenX = cb.clientBounds["centerX"]
            cenY = cb.clientBounds["centerY"]
            targetX = cenX-path[1]["x"]
            targetY = cenY-path[1]["y"]
            hm.realMoveToLocation(targetX,targetY)
            hm.clickAtCurrentLocation()
            time.sleep(step["waitTime"])
            

path = []
previousTime = time.time()
firstStep = True
travelDelay = 0
utils.findClientBounds()
recording = False
# setupNavigation()
readPathFile()