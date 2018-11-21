import findImg as fim
import random
import time
import clientBounds as cb
import utils
import pyautogui
import pynput
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key, Controller
import _pickle as cPickle
from threading import _start_new_thread
import HumanMouse as hm
from multiprocessing.pool import ThreadPool



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
    global previousTimeMouse
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
            prevTime = getPrevTimeMouse()
            travelDelay = time.time() - prevTime
            previousTimeMouse = time.time()
            print('timedelay is {0}'.format(travelDelay))
            step = {
                "x":cb.clientBounds["centerX"]-x,
                "y":cb.clientBounds["centerY"]-y,
                "waitTime": travelDelay
            }
            mousePath.append(step)
            print('Path: {0}'.format(mousePath))
            # travelTime = time.time()
    else:
        pass
def getPrevTimeMouse():
    return previousTimeMouse
def getPrevTimeKeyboard():
    return previousTimeKeyboard

def on_press(key):
    global recording
    global previousTimeKeyboard
    global keyPressDurationStart
    global cameraStep
    global keyReleased

    if key == Key.backspace:
        recording = True
        print('Recording')
        print(recording)
    elif key == Key.end:
        recording = False
        print('Stopped recording')
        writeCameraPathToFile()
        writeMousePathToFile()
    elif key != Key.backspace and key != Key.end and recording == True:
        prevTime = getPrevTimeKeyboard()
        moveDelay = time.time() - prevTime
        previousTimeKeyboard = time.time()
        if getKeyReleaseState():
            keyPressDurationStart = time.time()
            keyReleased = False
        cameraStep={
            "key":key,
            "waitTime":moveDelay
        }
        

def getKeyReleaseState():
    return keyReleased
def on_release(key):
    global cameraStep
    global keyReleased
    if recording and key != Key.end and key != Key.backspace:
        keyDuration = time.time() - keyPressDurationStart
        cameraStep["duration"] = keyDuration
        cameraPath.append(cameraStep)
        keyReleased = True
        cameraStep = {}

def setupNavigation():
    # utils.findClientBounds()
    pyautogui.moveTo(cb.clientBounds["centerX"],cb.clientBounds["centerY"])
    target = {
        "clientBounds":cb.clientBounds,
        "compassStartDeg":0,
        "start":'test',
        "target":'test'
    }
    mousePath.append(target)

    with mouse.Listener(on_click=on_click) as listener:
        with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
            listener.join()

def writeMousePathToFile():
    global mousePath
    fileName = '{0}_to_{1}_mouse.p'.format(mousePath[0]["start"],mousePath[0]["target"])
    cPickle.dump(mousePath,open(fileName,"wb"))
    print('Path written to file')
    mousePath = []

def readMousePathFile():
    # global mousePath
    path = cPickle.load(open("test_to_test_mouse.p","rb"))
    print('Loaded path as {0}'.format(path))
    print('Path starts at: {0}'.format(path[0]["start"]))
    navigatePath(path)

def writeCameraPathToFile():
    global cameraPath
    fileName = '{0}_to_{1}_camera.p'.format(mousePath[0]["start"],mousePath[0]["target"])
    cPickle.dump(cameraPath,open(fileName,"wb"))
    print('Path written to file')
    cameraPath = []

def readCameraPathFile():
    global cameraPath
    cameraPath = cPickle.load(open("test_to_test_camera.p","rb"))
    print('Loaded path as {0}'.format(cameraPath))
    moveCamera()

def navigatePathFile():
    # _start_new_thread(readCameraPathFile)
    readMousePathFile()
    _start_new_thread(navigatePath)
    # readCameraPathFile()

def navigatePath():
    # global mousePath
    path = cPickle.load(open("test_to_test_mouse.p","rb"))
    print('Loaded path as {0}'.format(path))
    print('Path starts at: {0}'.format(path[0]["start"]))
    # navigatePath()

    if path != []:
        print('Navigating path....')
        pathInfo = path[0]
        print(path)
        del path[0]
        print('Path is now: {0}'.format(path))
        for step in path:
            cenX = cb.clientBounds["centerX"]
            cenY = cb.clientBounds["centerY"]
            targetX = cenX-step["x"]
            targetY = cenY-step["y"]
            hm.realMoveToLocation(targetX,targetY)
            # pyautogui.moveTo(targetX,targetY)
            hm.clickAtCurrentLocation()
            time.sleep(step["waitTime"])

def moveCamera():
    if cameraPath != []:
        print('Moving camera along path....')
        for step in cameraPath:
            if "key" not in step:
                continue
            key = step["key"].char
            holdTime = step["duration"]
            start = time.time()
            while time.time() - start < holdTime:
                pyautogui.keyDown(key)
            pyautogui.keyUp(key)
            time.sleep(float(step["waitTime"]))

cameraStep = {}
mousePath = []
cameraPath = []
keyReleased = True
previousTimeMouse = time.time()
previousTimeKeyboard = time.time()
keyPressDurationStart = time.time()
firstStep = True
travelDelay = 0
utils.findClientBounds()
recording = False
# setupNavigation()
# readCameraPathFile()
# navigatePathFile()

readMousePathFile()