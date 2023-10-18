import pyautogui
import time
while True:
    with open("position.txt", "a") as file1:
        # Writing data to a file
        string = str(pyautogui.position())

        file1.write(f"\n{string.strip('Point')}")
        print(pyautogui.position())
        time.sleep(3)