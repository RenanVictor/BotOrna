import time
import pyautogui as pg
#import wx
#import win32gui as wg




#pg.locateOnWindow(title='Sem título - Paint')
#print(wg.GetWindowText(wg.GetForegroundWindow()))
#print(wg.GetForegroundWindow())
#print(wg.FindWindow(None, 'botOrna.py - Python - Visual Studio Code'))
#wg.ShowWindow(0,131796)


#tela = screenWidth, screenHeight = pg.size()
#mouse_position = currentMouseX, currentMouseY = pg.position()

#button7location = pg.locateOnScreen('calc7key.png',grayscale=True,confidence=0.5)
#print(button7location)
#xposition, yposition = pg.locateCenterOnScreen("WARRIORSDANCE.png",confidence=0.5)
#pg.click(xposition,yposition, duration= 1.0)
#time.sleep(2)
#xposition, yposition = pg.locateCenterOnScreen("Button_Battle.png",confidence=0.5)
#pg.click(xposition,yposition, duration= 1.0)

def start_Arena():
    xposition, yposition = pg.locateCenterOnScreen("HOLD_TO_SPAR.png",confidence=0.5)
    pg.moveTo(xposition,yposition,duration=0.5)   
    time.sleep(1.2)
    pg.mouseDown()
    time.sleep(4)
    pg.mouseUp()

def battle_arena():
    xposition, yposition = pg.locateCenterOnScreen("WARRIORSDANCE.png",confidence=0.5,grayscale = True)
    pg.click(xposition,yposition,duration=0.5)
    

battle_arena()