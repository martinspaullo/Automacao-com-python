import pyautogui
import time

pyautogui.press('winleft') #preciona a tecla windows
time.sleep(2)
pyautogui.write('firefox') #pesquisa por firefox
time.sleep(2)
pyautogui.press('enter') #pressiona enter
time.sleep(2)
pyautogui.moveTo(317,61)
time.sleep(2)
pyautogui.click()
pyautogui.write('youtube one bit code')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveTo(281,303)
time.sleep(2)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(652,524)
time.sleep(2)
pyautogui.click()
pyautogui.alert(text='Obrigado por se inscrever nesse canal', title='Agradecimento', button='OK')