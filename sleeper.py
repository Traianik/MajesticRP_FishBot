
import ctypes
import pydirectinput
from time import sleep, time
import random
import win32gui, win32con, win32api
from win32com.client import DispatchEx # Note - "Dispatch" opens in existing instance of Excel, "DispatchEx" opens in new instance



def move_screen():
    hwnd = win32gui.FindWindow('51030', None)
    win32gui.MoveWindow(hwnd, -10, 0, 800, 600, True)
    sleep(1)
    pydirectinput.click(x=360, y=289)
    sleep(1)

def sleep_pose():
    pydirectinput.keyDown('x')
    random_nuber = random.randint(0,3)
    print("We will sleep in pose number: ", random_nuber)
    if random_nuber == 0:
        pos0 = pydirectinput.click(x=246, y=200)
    if random_nuber == 1:
        pos1 = pydirectinput.click(x=223, y=316)
    if random_nuber == 2:
        pos2 = pydirectinput.click(x=274, y=417)
    if random_nuber == 3: 
        pos3 = pydirectinput.click(x=391, y=468)
    pydirectinput.keyUp('x')
    print("Sleeping!")


    
def randommove():
    x = random.randint(1,6)
    print(f"Making {x} random moves!")
    for i in range(x):  
        move_keys = ['w', 'a', 's', 'd']
        random_move = random.choice(move_keys)
        pydirectinput.press(random_move)
        sleep(0.3) 


# food_dict = {
#     1: [pydirectinput.doubleClick(x=521, y=94),pydirectinput.doubleClick(x=521, y=170)],
#     2: [pydirectinput.doubleClick(x=556, y=91),pydirectinput.doubleClick(x=556, y=167)],
#     3: [pydirectinput.doubleClick(x=593, y=93),pydirectinput.doubleClick(x=593, y=168)],
#     4: [pydirectinput.doubleClick(x=630, y=96),pydirectinput.doubleClick(x=630, y=169)],
#     5: [pydirectinput.doubleClick(x=667, y=96),pydirectinput.doubleClick(x=667, y=173)],
#     6: [pydirectinput.doubleClick(x=665, y=131),pydirectinput.doubleClick(x=665, y=201)],
#     7: [pydirectinput.doubleClick(x=629, y=131),pydirectinput.doubleClick(x=629, y=202)],
#     8: [pydirectinput.doubleClick(x=594, y=129),pydirectinput.doubleClick(x=594, y=199)],
#     9: [pydirectinput.doubleClick(x=558, y=131),pydirectinput.doubleClick(x=558, y=199)],
#     10: [pydirectinput.doubleClick(x=521, y=132),pydirectinput.doubleClick(x=521, y=199)]
# }

    

def drink_eat(i):
    pydirectinput.press('i')
    sleep(1)
    if i == 1:
        pydirectinput.tripleClick(x=521, y=94)
        sleep(6)
        pydirectinput.tripleClick(x=521, y=170)
        sleep(6)
    if i == 2:
        pydirectinput.tripleClick(x=556, y=91)
        sleep(6)
        pydirectinput.tripleClick(x=556, y=167)
        sleep(6)
    if i == 3:
        pydirectinput.tripleClick(x=593, y=93)
        sleep(6)
        pydirectinput.tripleClick(x=593, y=168)
        sleep(6)
    if i == 4:
        pydirectinput.tripleClick(x=630, y=96)
        sleep(6)
        pydirectinput.tripleClick(x=630, y=169)
        sleep(6)
    if i ==5 :
        pydirectinput.tripleClick(x=667, y=96)
        sleep(6)
        pydirectinput.tripleClick(x=667, y=173)
        sleep(6)
    if i == 6:
        pydirectinput.tripleClick(x=665, y=131)
        sleep(6)
        pydirectinput.tripleClick(x=665, y=201)
        sleep(6)
    if i == 7:
        pydirectinput.tripleClick(x=629, y=131)
        sleep(6)
        pydirectinput.tripleClick(x=629, y=202)
        sleep(6)
    if i == 8:
        pydirectinput.tripleClick(x=594, y=129)
        sleep(6)
        pydirectinput.tripleClick(x=594, y=199)
        sleep(6)
    if i == 9:
        pydirectinput.tripleClick(x=558, y=131)
        sleep(6)
        pydirectinput.tripleClick(x=558, y=199)
        sleep(6)
    if i == 10:
        pydirectinput.tripleClick(x=521, y=132)
        sleep(6)
        pydirectinput.tripleClick(x=521, y=199)
        sleep(6) 
    pydirectinput.press('i')
    sleep(1) 





i = 0
drink_food = 1

while True:
    print("Starting anti-afk script")
    move_screen()
    randommove()
    if i % 7 == 0:
        print("Drinkig and Eating.")
        drink_eat(drink_food)
        drink_food+=1
    sleep_pose()
    rnd_sleep = random.randint(500,720)
    print(f"Next move in {rnd_sleep} seconds.")
    sleep(rnd_sleep) 
    i+=1
    print(f"Ending cycle number: {i}.")