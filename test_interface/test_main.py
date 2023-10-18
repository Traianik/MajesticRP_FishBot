import cv2 as cv
import numpy as np
import os
import time 
from windowcapture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter
import pydirectinput
import mss
import pyautogui
import time
import datetime


# initialize the WindowCapture class
#wincap = WindowCapture('RАGЕ Multiрlayеr   ')  
# wincap = WindowCapture("game.png - Paint")  
# #wincap = WindowCapture()  
# vision_limestone = Vision('fishPhotoshop.png') 
# vision_limestone.init_control_gui()



# initialize the WindowCapture class
# wincap = WindowCapture('LOC2.jpg - Paint')
wincap = WindowCapture('RАGЕ Multiplaуer   ')   
# initialize the Vision class
#test = Vision('images/fishPhotoshop.jpg')  
loc1 = Vision('images/fishPhotoshop.jpg')  
loc2 = Vision('images/loc2.jpg') 

# initialize the trackbar window
# vision_limestone.init_control_gui()

# limestone HSV filter
#hsv_filter = HsvFilter(50, 0, 188, 174, 255, 255, 0, 0, 0, 5)
#hsv_filter = HsvFilter(0, 0, 188, 130, 45, 255, 15, 0, 0, 4)
#hsv_filter = HsvFilter(34, 0, 163, 153, 255, 255, 0, 255, 0, 3) 
hsv_filter = HsvFilter(0, 0, 160, 153, 255, 255, 0, 255, 0, 7)  


dimensions_lkm = {
        'left': 0, 
        'top': 0,
        'width': 400,
        'height': 100
    }

uderjivatee = cv.imread('images/lkm.png')  

w_lkm = uderjivatee.shape[1]
h_lkm = uderjivatee.shape[0]




sct = mss.mss()

def gather_fish(location,threshhold):

    i =  0
    directionfish = None 
    pressed = 'no' 
    old_loc = None
    start = None
    fcount = 0
    start_time = datetime.datetime.now()
    last = start_time
    time_nr = 0



    loop_time = time.time()
    vision = None
    sleep_time = None
    if location == 1:
        vision = loc1
        sleep_time = 15
    if location == 2:
        vision = loc2
        sleep_time = 18
    while(True):

        # get an updated image of the game
        screenshot = wincap.get_screenshot() 

        # pre-process the image
    # proccesed_image = vision_limestone.apply_hsv_filter(screenshot, hsv_filter) 

        # do object detection 
        rectangles = vision.find(screenshot, threshold=threshhold) 


        output_image = vision.draw_rectangles(screenshot, rectangles)
    

        #cv.imshow('Proccessed', proccesed_image)
        cv.imshow('Matches', output_image) 

        if len(rectangles) > 0:
            targets = vision.get_click_points(rectangles)
            target = wincap.get_screen_position(targets[0])
            print(f"X = {target[0]} Y= {target[1]}")
            i = i + 1
            if i >= 2:
                if old_loc != None:
                    print("Fish este: ",target[0])  
                    
                    if(old_loc<target[0]):  
                            print("Right")  

                            if pressed == 'no':
                                pydirectinput.keyDown('a')
                                print("----Pressed Right-----")
                                directionfish = "Right"
                                pressed = 1  
                                

                            if directionfish =="Left":
                                print("Direction of the fish was Left now it's Right")
                                pydirectinput.keyUp('d') 
                                print("Button d was pressed up")


                                print("PR2 Created!")
                                pydirectinput.keyDown('a')
                                print("----Pressed Left-----")
                                directionfish = "Right" 
                                pressed += 1


                    if(old_loc>target[0]):  
                            print("Left") 
                            if pressed == 'no':
                                pydirectinput.keyDown('d')
                                print("----Pressed Left-----")
                                directionfish = "Left"
                                pressed = 1
    

                            if directionfish =="Right":
                                print("Direction of the fish was Right now it's Left")
                                pydirectinput.keyUp('a')
                                print("Button a was pressed up")

                                print("PL 2 created!")
                                pydirectinput.keyDown('d')
                                print("----Pressed Right-----")
                                directionfish = "Left"
                                pressed += 1


            print("Old loc",old_loc)
            print("now loc",target[0])
            old_loc = target[0]

        scr2 = np.array(sct.grab(dimensions_lkm))

        # Cut off alpha
        scr_remove2 = scr2[:,:,:3]
        result2 = cv.matchTemplate(scr_remove2, uderjivatee, cv.TM_CCOEFF_NORMED)
        _, max_val_lkm, _, max_loc_lkm = cv.minMaxLoc(result2)
        src2 = scr2.copy()

        if max_val_lkm >0.65:
            cv.rectangle(src2,max_loc_lkm,(max_loc_lkm[0] + w_lkm, max_loc_lkm[1] + h_lkm), (0,255,255), 2)
            cv.waitKey(1) 
            print("uderjivaete") 
            print(max_loc_lkm)
            pydirectinput.keyUp('a')  
            pydirectinput.keyUp('d') 
            pyautogui.mouseDown()
            time.sleep(sleep_time)

            #time.sleep(15)  #pos 1 ,
            #time.sleep(13) # pos 2
            #time.sleep(11)  #pos 11 
            
            pyautogui.mouseUp()
            pydirectinput.press('e') 
            fcount = fcount+1
            pressed = 'no' 
            old = 0
            i = 0 
            time_nr = 0


            directionfish = None
            now = datetime.datetime.now()
            print(f"Fish #{fcount} eplased time:{str(now-start_time)}")


        # debug the loop rate
        print('FPS {}'.format(1 / (time.time() - loop_time)))
        loop_time = time.time()

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

        now = datetime.datetime.now()
        if now - last > datetime.timedelta(seconds=1):
            last = now
            time_nr += 1
            if time_nr > 80:
                pydirectinput.keyUp('a')  
                pydirectinput.keyUp('d') 
                pyautogui.mouseUp()
                print("fish not found after 80 seconds! breaking the loop!w")
                break
print('Done.') 


gather_fish(2,0.75)










# loop_time = time() 
# while(True):

#     # get an updated image of the game
#     screenshot = wincap.get_screenshot()

#     cv.imshow('Computer Vision', screenshot) 

#     # debug the loop rate
#     print('FPS {}'.format(1 / (time() - loop_time)))
#     loop_time = time()

#     # press 'q' with the output window focused to exit.
#     # waits 1 ms every loop to process key presses
#     if cv.waitKey(1) == ord('q'):
#         cv.destroyAllWindows()
#         break

# print('Done.')