import pyautogui
from time import sleep

with open("files/alunos.txt", "r", encoding="utf-8") as file: #Abrindo o arquivo aluno.txt
    for line in file:
        aluno = line.split(',')[0]
        email = line.split(',')[1]
        pyautogui.click(942, 277, duration=1)
        pyautogui.write(aluno)
        pyautogui.click(952, 318, duration=1)
        pyautogui.write(email)
        pyautogui.click(958, 344, duration=0.5)
        pyautogui.screenshot(f'files/img/{aluno}.png')
        sleep(1)
    
    