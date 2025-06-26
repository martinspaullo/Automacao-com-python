import pyautogui
import time

# pyautogui.moveTo(1807,18)
# time.sleep(1)
# pyautogui.click()
# time.sleep(1)
# pyautogui.screenshot('exemplo2.png')


# A cada 3 segundos gera um screenshort
while True:
    pyautogui.screenshot(f"print_{time.time()}.png")
    time.sleep(3)
