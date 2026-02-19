import pyautogui
import time
import random

# 10 second delay before starting
print("Starting in 10 seconds... Switch to the target window.")
time.sleep(10)

while True:
    # Type /coin
    pyautogui.write('/coin')
    time.sleep(0.2)

    # Press TAB
    pyautogui.press('tab')
    time.sleep(0.2)

    # Randomly choose heads or tails
    choice = random.choice(['heads', 'tails'])
    pyautogui.write(choice)
    time.sleep(0.2)

    # Press TAB again
    pyautogui.press('tab')
    time.sleep(0.2)

    # Type 200
    pyautogui.write('200')
    time.sleep(0.2)

    # Press ENTER
    pyautogui.press('enter')

    # Wait 2 seconds before repeating
    time.sleep(2)
