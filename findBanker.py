import findImg as fim
import utils
import os
import pyautogui
import time
import mss
import mss.tools
import HumanMouse as hm
import random
from datetime import datetime
import cv2

def findBanker():

    clientData = utils.findClientBounds()

    bankerOffSets = {
         "banker":{
            "x":0,
            "y":-110
        },
        "banker1":{
            "x":20,
            "y":0
        },
         "banker2":{
            "x":20,
            "y":0
        },
         "banker3":{
            "x":0,
            "y":-100
        },
         "banker4":{
            "x":20,
            "y":-50
        }
    }
    
    # target = pyautogui.locateOnScreen('banker.png',region=(clientData["topLeft"][0],clientData["topLeft"][1],clientData["bottomRight"][0]-clientData["bottomLeft"][0],clientData["bottomRight"][1]-clientData["topLeft"][1]))
    # pyautogui.locateOnScreen('banker.png')

    # fim.locateImgOnScreenAndClick('banker.png',True)
    # targetX, targetY = pyautogui.center(target)
    # hm.realMoveToLocation(targetX,targetY)
    # fim.locateImgOnScreenAndClick('banker',True)

    print("finding banker....")
    pyautogui.keyDown('s')
    pyautogui.PAUSE = 2
    pyautogui.keyUp('s')
    pyautogui.PAUSE = 0
    hm.realMoveToLocation(clientData["centerX"]+random.randint(0,30), clientData["centerY"]-random.randint(80,140))
    banker = fim.locateImgOnScreenAndClick('banker',True)
    while banker == None:
        print('locating....')
        random.seed(datetime.now())
        hm.realMoveToLocation(clientData["centerX"]+random.randint(0,100), clientData["centerY"]-random.randint(80,140))
        time.sleep(random.randint(2,6)/4)
        # banker = fim.locateImgOnScreenAndClick('banker',True)
        banker = pyautogui.locateOnScreen('banker3.png',confidence=0.7)
        count = 0
        while banker ==None:
            print('trying hard')
            banker = pyautogui.locateOnScreen('banker3.png')
            count+=1
            if count >= 5:
                break
        if banker != None:
            print('found!')
            # bankerX, bankerY = 
            bankerX, bankerY = pyautogui.center(banker)
            pyautogui.click(bankerX,bankerY)

    # time.sleep(2)
    # files = os.listdir('{0}/imgs/{1}'.format(os.getcwd(),'banker'))
    # for imgName in files:
    #     # counter = 0
    #     # while counter <= 1:
    #         # pyautogui.keyDown('d')
    #     banker = pyautogui.locateOnScreen('{0}/imgs/banker/{1}'.format(os.getcwd(),imgName))
    #         # counter2 = 0
    #         # while banker == None:
    #         #     print('Locating....')
    #         #     banker = pyautogui.locateOnScreen('{0}/imgs/banker/{1}'.format(os.getcwd(),imgName))
    #         #     if banker != None:
    #         #         bankerX, bankerY = pyautogui.center(banker)
    #         #         pyautogui.click(bankerX,bankerY)
    #         #         break
    #         #     if counter2 >=1:
    #         #         print('Could not find image')
    #         #         break
    #         #     else:
    #         #         # pyautogui.keyDown('d')
    #         #         # pyautogui.keyUp('d')
    #         #         counter2+=1
    #         # counter += 1
    #     if banker != None:
    #         print('found {0}'.format(imgName))
    #         bankerX, bankerY = pyautogui.center(banker)
    #         clickX = bankerX + bankerOffSets[imgName]["x"]
    #         clickY = bankerY + bankerOffSets[imgName]["y"]
    #         hm.realMoveToLocation(clickX,clickY)
    #             # pyautogui.click()

    # searchAreaLeft = clientData["centerX"]/4
    # searchAreaRight = clientData["centerX"] + (clientData["centerX"]/2)
    # searchAreaTop   = clientData["centerY"] + (clientData["centerY"]/2)
    # searchAreaBottom = clientData["centerY"] - (clientData["centerY"]/2)

    # random.seed(datetime.now())
    # hm.realMoveToLocation(clientData["centerX"]+random.randint(0,20),clientData["centerY"]-random.randint(30,40))

    # fim.locateImgOnScreenAndClick('banker',True)

    # print("Moving to search left")
    # pyautogui.moveTo(clientData["centerX"]-searchAreaLeft,clientData["centerY"])

    # print("Moving to search left")

    # print('resetting camera...')
    # pyautogui.keyDown('s')
    # pyautogui.PAUSE=2
    # pyautogui.keyUp('s')
    # print('camera reset')
    # print('Moving camera to search position')
    # pyautogui.keyDown('w')
    # pyautogui.PAUSE = 1
    # pyautogui.keyUp('w')
    # fim.locateImgOnScreenAndClick('banker',True)
    # print("finding banker....")
    # time.sleep(2)
    # files = os.listdir('{0}/imgs/{1}'.format(os.getcwd(),'banker'))
    # for imgName in files:
    #     counter = 0
    #     while counter <= 1:
    #         # pyautogui.keyDown('d')
    #         banker = pyautogui.locateOnScreen('{0}/imgs/banker/{1}'.format(os.getcwd(),imgName))
    #         counter2 = 0
    #         while banker == None:
    #             print('Locating....')
    #             banker = pyautogui.locateOnScreen('{0}/imgs/banker/{1}'.format(os.getcwd(),imgName))
    #             if banker != None:
    #                 bankerX, bankerY = pyautogui.center(banker)
    #                 pyautogui.click(bankerX,bankerY)
    #                 break
    #             if counter2 >=1:
    #                 print('Could not find image')
    #                 break
    #             else:
    #                 # pyautogui.keyDown('d')
    #                 # pyautogui.keyUp('d')
    #                 counter2+=1
    #         counter += 1
    # # fim.locateImgOnScreenAndClick('banker',True)

findBanker()