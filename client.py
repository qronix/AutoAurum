import pyautogui
# import pyscreenshot as ImageGrab
import PIL
import psutil
import pynput
import findImg
import config
import time
import utils
import findBanker
from pynput.mouse import Listener
import HumanMouse as hm

def init():
        foundClient = False
        print('Looking for RuneScape client')
        for pid in psutil.pids():
            try:
                process = psutil.Process(pid)
                if "RuneScape.exe" in process.name():
                    print('Runescape client found')
                    foundClient = True
                    setup()
                    return True
                else:
                    pass
            except:
                continue
        if(foundClient==False):
            print('Runescape client was not found. Please launch the client and restart AutoAurum')

def setup():
    print('Please close all windows besides this and Runescape')
    print('Logging in......')
    # moveTest()
    # utils.findClientBounds()
    findBanker.findBanker()
    # try:
    #     login()
    # except Exception as ex:
    #     print(ex)

def moveTest():
    hm.realMoveToLocation(2540,1377)

def login():
    try:
        findImg.locateImgOnScreenAndClick('loginLogo1',True)
        username = config.config['username']
        password = config.config['password']
        pyautogui.typewrite(username,0.2)
        time.sleep(2)
        pyautogui.press('tab')
        pyautogui.typewrite(password,0.1)
        findImg.locateImgOnScreenAndClick('loginButton',True)
        enterWorld()
    except Exception as ex:
        print(ex)

def enterWorld():
    print("Entering world....")
    findImg.locateImgOnScreenAndClick('playButton',True)
    time.sleep(4)
    findImg.locateImgOnScreenAndClick('homeButtonMap',False)
    print("Entered world")
    utils.findClientBounds()

if __name__ == '__main__':
    
    init()

