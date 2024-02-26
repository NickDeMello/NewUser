# New user Creation Salesforce

import pyautogui
#import pandas as pd
import os
import cv2
import numpy as np
import GUI
from time import sleep
import WorkingOCR


# Helpers
def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)
    
def find(button):
    for i in range(5):
        screenshot = pyautogui.screenshot()
        screenshot_cv = np.array(screenshot)
        screenshot_cv = cv2.cvtColor(screenshot_cv, cv2.COLOR_RGB2BGR)
        template = cv2.imread(button)
        result = cv2.matchTemplate(screenshot_cv, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        min_val, max_val, min_loc, top_left = cv2.minMaxLoc(result)
        print(max_val)
        if max_val > threshold:
            h, w, _ = template.shape
            click_button = [top_left[0] + w/2, top_left[1] + h/2]
            return click_button
    raise Exception("button not found")

def stall(t):
    pyautogui.PAUSE = float(t/4)
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth/2, screenHeight/2)
    pyautogui.move(200, 10)
    pyautogui.move(-400, 10)
    pyautogui.move(200, 10)
    pyautogui.PAUSE = 0.2
    pyautogui.moveTo(100,100)
    
# Procedural
def OpenEdge():
    pyautogui.PAUSE = 1
    pyautogui.press("win")
    #pyautogui.PAUSE = 1
    sleep(1)
    addToClipBoard('https://service.danfoss.net/esc?id=favorites_list')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")
    
def OpenTicketPage():
    pyautogui.PAUSE = 1
    addToClipBoard('https://service.danfoss.net/esc?id=favorites_list')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")

def type_description(description):
    full = ""
    for line in description:
        #pyautogui.write(line)
        full = full + line
    pyautogui.write(full, interval=0.02)

def Run():
    subject = GUI.BackEnd.fetch(0)
    description = GUI.BackEnd.fetch(1)
    sleep(1)
    OpenEdge()
    #OpenTicketPage()
    sleep(5)
    #coord = find(button)
    pyautogui.click(WorkingOCR.tripple_try("Salesforce"))
    sleep(3)
    pyautogui.scroll(-400)
    pyautogui.click(WorkingOCR.box_under_word("Subject", 40))
    pyautogui.write(subject)
    pyautogui.click(WorkingOCR.tripple_try("CSC"))
    pyautogui.click(WorkingOCR.tripple_try("DPD"))
    pyautogui.click(WorkingOCR.box_under_word("Description", 100))
    type_description(description)
    
    pyautogui.moveTo(WorkingOCR.tripple_try("Submit"))
    
    #pyautogui.click()

GUI.runGUI()
Run()

