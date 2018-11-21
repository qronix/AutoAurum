import pyautogui
import findImg as fim
import math
import clientBounds as cb
import time

def findClientBounds():
    time.sleep(2)
    topLeft = fim.getImgCoords('clientTopLeft',None)
    bottomRight = fim.getImgCoords('clientBottomRight',None)
    bottomLeft = [bottomRight[1],topLeft[0]]
    topRight  = [bottomRight[0],topLeft[1]]

    centerX = bottomLeft[0]+((bottomRight[0]-bottomLeft[0])/2)
    centerY = bottomRight[1]-(bottomRight[1]-topLeft[1])/2

    # pyautogui.moveTo(centerX,centerY)

    clientBounds = {
        "topLeft":topLeft,
        "bottomRight":bottomRight,
        "bottomLeft":bottomLeft,
        "topRight":topRight,
        "centerX":centerX,
        "centerY":centerY
    }
    cb.clientBounds = clientBounds
    print('Client bounds : {0}'.format(cb.clientBounds))
    findMapBounds()
    # return clientBounds
def findMapBounds():
    compassLeftSideCoords = fim.getImgCoords('compassLeftSide',None)
    compassBottomLeft = [compassLeftSideCoords[0]-20,compassLeftSideCoords[1]+20]
    myRegion = {
        "topLeftX":cb.clientBounds["topLeft"][0],
        "topLeftY":cb.clientBounds["topLeft"][1],
        "width":(cb.clientBounds["bottomRight"][0]-cb.clientBounds["topLeft"][0]),
        "height":(cb.clientBounds["bottomRight"][1]-cb.clientBounds["topLeft"][1])
    }
    compassTopRightCoords = pyautogui.locateOnScreen('homeButtonMap.png',region=(cb.clientBounds["topLeft"][0],cb.clientBounds["topLeft"][1],cb.clientBounds["bottomRight"][0]-cb.clientBounds["topLeft"][0],cb.clientBounds["bottomRight"][1]-cb.clientBounds["topLeft"][1]),confidence=0.9)
    compassTopRightX, compassTopRightY = pyautogui.center(compassTopRightCoords)
    print('My region: {0}'.format(myRegion))
    mapBounds = {
        "topRight": [compassTopRightX+20,compassTopRightY-20],
        "bottomLeft" : compassBottomLeft
    }
    cb.mapBounds = mapBounds
    
    print('Map bounds : {0}'.format(cb.mapBounds))

def catalogCompass():
    # pyautogui.screenshot()
    holdTime = 0.1
    
    # takes 24 key presses at 0.1 second delay to rotate camera 360 degrees
    # 15 degrees per key press
    counter = 0
    degree = 15
    while counter <60:
        time.sleep(0.5)
        pyautogui.screenshot('compass_{}_degrees.png'.format(degree*counter),region=(cb.mapBounds["bottomLeft"][0],cb.mapBounds["topRight"][1],cb.mapBounds["topRight"][0]-cb.mapBounds["bottomLeft"][0],cb.mapBounds["bottomLeft"][1]-cb.mapBounds["topRight"][1]))
        start = time.time()
        print('Counter is at {0}'.format(counter))
        while time.time() - start < holdTime:
            pyautogui.keyDown('d')
        pyautogui.keyUp('d')
        counter+=1

# findClientBounds()
def moveCompass(degrees,capture):
    holdTime = 0.1
    counter = degrees/15
    while counter > 0:
        start = time.time()
        while time.time() - start < holdTime:
            pyautogui.keyDown('d')
        pyautogui.keyUp('d')
        if capture == True:
            pyautogui.screenshot('compass_{}_degrees.png'.format(degrees),region=(cb.mapBounds["bottomLeft"][0],cb.mapBounds["topRight"][1],cb.mapBounds["topRight"][0]-cb.mapBounds["bottomLeft"][0],cb.mapBounds["bottomLeft"][1]-cb.mapBounds["topRight"][1]))
        counter-=1

# findClientBounds()
# moveCompass(120,False)
# time.sleep(2)
# targetX, targetY = fim.getImgCoords('compass_120_deg',None)
# pyautogui.moveTo(targetX,targetY)
# catalogCompass()
