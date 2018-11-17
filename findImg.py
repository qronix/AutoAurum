import pyautogui as pg
import os
import HumanMouse as hMouse

imgDirectory = '/imgs/'
def findImg(name):
    try:
        path = '{0}{1}{2}.png'.format(os.getcwd(),imgDirectory,name)
        if os.path.isfile(path):
            locateImgOnScreen(path)
    except Exception as ex:
        print('Could not find file')
        print(ex)

def locateImgOnScreen(imgPath):
    target = pg.locateOnScreen(imgPath)
    attempts = 0
    while target == None:
        print('Attempting to locate image on screen...')
        target = pg.locateOnScreen(imgPath)
        pg.PAUSE = 1
        attempts+=1
        if(attempts>=10):
            print('Could not locate image on screen.')
            break
    if target != None:
        targetX, targetY = pg.center(target)
        hMouse.realMoveToLocation(targetX,targetY)
