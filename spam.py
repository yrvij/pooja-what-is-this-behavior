import pyautogui
import time
script = []

file = open('pooja.txt','r')
while True:
    line = file.readline().strip()
    script.append(line)
    if not line:
        break

file.close()
lastpart = script[len(script)-4:]
script = script[:len(script)-4]

for dialogue in script:
    pyautogui.write(dialogue)
    pyautogui.PAUSE = 0.38
    pyautogui.press('enter')

time.sleep(1)

for entry in lastpart:
    pyautogui.write(entry)
    pyautogui.PAUSE = 0.42
    pyautogui.press('enter')

pyautogui.write('Please like and follow. This took a while!!')
