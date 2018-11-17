import pyautogui
# import pyscreenshot as ImageGrab
import PIL
import psutil
import pynput
import findImg
import config
from pynput.mouse import Listener

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
    # findImg.findImg('magicShortBow')
    # findBow()
    # login()
    # print('Logging')
    # login()
    # with Listener(on_click=on_click) as listener:
    #     listener.join()
def findBow():
    bow = pyautogui.locateOnScreen('magicShortBow.png')
    while bow == None:
        bow = pyautogui.locateOnScreen('magicShortBow.png')
        print('finding bow')
        print(bow)
    bowX, bowY = pyautogui.center(bow)
    pyautogui.click(bowX,bowY)
    print(bow)
def login():
    loginButton = pyautogui.locateOnScreen('loginButton.png')
    while loginButton == None:
        loginButton = pyautogui.locateOnScreen('loginButton.png')        
    print(loginButton)
    loginButtonX, loginButtonY = pyautogui.center(loginButton)
    pyautogui.click(loginButtonX,loginButtonY)
    username = config.config['username']
    password = config.config['password']
    pyautogui.typewrite(username)
    pyautogui.PAUSE = 1
    pyautogui.press('tab')
    pyautogui.typewrite(password)
    pyautogui.click(loginButtonX, loginButtonY)
    pyautogui.PAUSE = 2
    enterWorld()
def enterWorld():
    print("Entering world")
    playButton = pyautogui.locateOnScreen('playButton.png')
    while playButton == None:
        playButton = pyautogui.locateOnScreen('playButton.png')
    playButtonX, playButtonY = pyautogui.center(playButton)
    pyautogui.click(playButtonX,playButtonY)
    pyautogui.PAUSE = 4
    reportButton = pyautogui.locateOnScreen('reportButton.png')
    while reportButton == None:
        print("Waiting to enter world....")
        pyautogui.PAUSE = 1
        reportButton = pyautogui.locateOnScreen('reportButton.png')
    print("Entered world")
    
def on_click(x,y,button,pressed):
    if not pressed:
        print('Mouse is at {0},{1}').format(x,y)
        image = pyautogui.screenshot('test.png')

if __name__ == '__main__':
    
    init()

