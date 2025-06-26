import pyautogui
import time

 
pyautogui.press('winleft') #clica no botao do windows
time.sleep(2)
pyautogui.write('calculadora') #Escreve calculadora
time.sleep(2)
pyautogui.press('enter') #pressiona enter
time.sleep(2)
pyautogui.hotkey('ctrl', 'shift', 'esc') 
time.sleep(2)
# with pyautogui.hold('alt'):
#     pyautogui.press(['f4'])
# time.sleep(2)
# with pyautogui.hold('alt'):
#     pyautogui.press(['f4'])
# time.sleep(2)
with pyautogui.hold('winleft'):
    pyautogui.press(['left'])
time.sleep(2)
pyautogui.click()
time.sleep(2)
with pyautogui.hold('winleft'):
    pyautogui.press(['right'])