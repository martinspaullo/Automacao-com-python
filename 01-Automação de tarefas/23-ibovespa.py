import pyautogui
import time

pyautogui.press('winleft')
time.sleep(2)
pyautogui.write('chrome')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveTo(247,90)
time.sleep(2)
pyautogui.click()
pyautogui.write('ibovespa hoje')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.screenshot('ibovespa.png')