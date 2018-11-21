import pyautogui
from PIL import Image
import os
import HumanMouse as hMouse
from pathlib import Path
# import utils
import clientBounds as cb
import cv2

# cb = utils.findClientBounds()
imgDirectory = '/imgs/'
def getPath(name):
    try:
        path = '{0}{1}{2}.png'.format(os.getcwd(),imgDirectory,name)
        osPath = Path(path)
        if osPath.exists():
            return path.replace('\\','/')
    except Exception as ex:
        print('Could not find file')
        print(ex)
        return False

def locateImgOnScreenAndClick(name,click):
    imgPath = getPath(name)

    if cb.clientBounds == {}:
        target = pyautogui.locateOnScreen(imgPath,confidence=0.9)
    else:
        target = pyautogui.locateOnScreen(imgPath,region=(cb.clientBounds["topLeft"][0],cb.clientBounds["topLeft"][1],cb.clientBounds["bottomRight"][0]-cb.clientBounds["topLeft"][0],cb.clientBounds["bottomRight"][1]-cb.clientBounds["topLeft"][1]),confidence=0.9)
    print('Searching for img')
    # attempts = 0
    # while target == None:
    #     print('Attempting to locate image on screen...')
    #     target = pyautogui.locateOnScreen(imgPath)
    #     # pyautogui.PAUSE = 1
    #     attempts+=1
    #     if(attempts<=1):
    #         print('Could not locate image on screen.')
    #         break
    if target != None and click == True:
        targetX, targetY = pyautogui.center(target)
        hMouse.realMoveToLocation(targetX,targetY)
    if target != None and click == False:
        return True

def getImgCoords(name,customRegion):
    imgPath = getPath(name)
    if cb.clientBounds == {} and customRegion == None:
        target = pyautogui.locateOnScreen(imgPath,confidence=0.8)
    elif cb.clientBounds != {} and customRegion == None:
        target = pyautogui.locateOnScreen(imgPath,region=(cb.clientBounds["topLeft"][0],cb.clientBounds["topLeft"][1],cb.clientBounds["bottomRight"][0]-cb.clientBounds["topLeft"][0],cb.clientBounds["bottomRight"][1]-cb.clientBounds["topLeft"][1]),confidence=0.8)
    elif cb.clientBounds != {} and customRegion != None:
        target = pyautogui.locateOnScreen(imgPath,region=(customRegion["topLeftX"],customRegion["topLeftY"],customRegion["width"],customRegion["height"]),confidence=0.8)
    if target != None:
        targetX, targetY = pyautogui.center(target)
        return [targetX,targetY]