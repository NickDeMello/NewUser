import pytesseract
import cv2
import pyautogui
import numpy as np
from time import sleep

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\U429604\\OneDrive - Danfoss\\Desktop\\Python\\Tesseract-OCR\\tesseract.exe"

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot_np

def search_boxes(boxes, target):
    if len(target) <= 2:
        return None
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
               word = b[11]
               #print(word)
               if target.lower() in word.lower():
                   x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                   middle_x = x + w // 2
                   middle_y = y + h // 2
                   return (middle_x, middle_y)
    return search_boxes(boxes, target[:-1])

def find_word(target):
    if len(target) <= 2:
        return None
    img = take_screenshot()
    boxes = pytesseract.image_to_data(img, lang='eng', config=r'--oem 1 --psm 11')
    return search_boxes(boxes, target)

def box_under_word(target, offset):
    my_tuple = tripple_try(target)
    ret_x = my_tuple[0]
    ret_y = my_tuple[1] + offset
    return (ret_x, ret_y)

def tripple_try(target):
    for i in range(3):
        ret = find_word(target)
        if ret is not None:
            return ret
        sleep(2)
    if ret is None:
        raise ValueError("Could not find " + target)
    return ret

"""
def find_word(target):
    if len(target) <= 2:
        return None
    img = take_screenshot()
    boxes = pytesseract.image_to_data(img, lang='eng', config=r'--oem 1 --psm 11')
    
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
               word = b[11]  # Extract the recognized word
               #print(word)
               if target.lower() in word.lower():
                   x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                   middle_x = x + w // 2
                   middle_y = y + h // 2
                   return (middle_x, middle_y)
    return find_word(target[:-1])

coord = box_under_word("Subject")
pyautogui.moveTo(coord)
print(coord)
"""
