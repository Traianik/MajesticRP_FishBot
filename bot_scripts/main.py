import cv2
import numpy
import pyautogui 
import time 
from PIL import ImageGrab
import pydirectinput
import mss
import keyboard
import datetime
# cv2.imshow('fish', fish_img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# cv2.imshow('Result', result)
# cv2.waitKey() 
# cv2.destroyAllWindows()

# result = cv2.matchTemplate(game_img, fish_img, cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# print(max_loc)
# print(max_val)

# w = fish_img.shape[1]
# h = fish_img.shape[0] 

# cv2.rectangle(game_img,max_loc,(max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)


def gather_fish(run:bool):

  sct = mss.mss()

  dimensions_lkm = {
          'left': 0, 
          'top': 0,
          'width': 400,
          'height': 100
      }

  dimensions_main = {
          'left': 0, 
          'top': 0,
          'width': 1920,
          'height': 1080
      }




  fish_img = cv2.imread('images/fish.png') #fish 1,  11 third person
  #fish_img = cv2.imread('images/fishPhotoshop.png') #11 photoshop first pirson  
  #fish_img = cv2.imread('images/photoshop-test1.png') #fish 7-8   
  uderjivatee = cv2.imread('images/lkm.png') 

  w = fish_img.shape[1]
  h = fish_img.shape[0]


  w_lkm = uderjivatee.shape[1]
  h_lkm = uderjivatee.shape[0]

  i =  0
  directionfish = None 
  pressed = 'no' 
  old_loc = None
  start = None
  window = None
  fcount = 0
  start_time = datetime.datetime.now()
  last = start_time
  time_nr = 0 
  loop_time = time.time()

  while run:
          
      scr = numpy.array(sct.grab(dimensions_main))

      # Cut off alpha
      scr_remove = scr[:,:,:3]
      result = cv2.matchTemplate(scr_remove, fish_img, cv2.TM_CCOEFF_NORMED)
      min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


      src = scr.copy()
      print(max_val) 
      if max_val >= 0.69:  
          cv2.rectangle(src,max_loc,(max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
          i = i + 1
          if i >= 2:
              if old_loc != None:
                  print("Fish detected",max_loc)  
                  
                  if(old_loc<max_loc): 
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


                  if(old_loc>max_loc):  
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
          print("now loc",max_loc)
          old_loc = max_loc

      scr2 = numpy.array(sct.grab(dimensions_lkm))

      # Cut off alpha
      scr_remove2 = scr2[:,:,:3]
      result2 = cv2.matchTemplate(scr_remove2, uderjivatee, cv2.TM_CCOEFF_NORMED)
      _, max_val_lkm, _, max_loc_lkm = cv2.minMaxLoc(result2)
      src2 = scr2.copy()

      if max_val_lkm >0.65:
          cv2.rectangle(src,max_loc_lkm,(max_loc_lkm[0] + w_lkm, max_loc_lkm[1] + h_lkm), (0,255,255), 2)
          cv2.imshow('Computer Vision', src)
          cv2.waitKey(1) 
          print("uderjivaete") 
          print(max_loc_lkm)
          pydirectinput.keyUp('a')  
          pydirectinput.keyUp('d') 
          pyautogui.mouseDown()
          time.sleep(17)  #pos 1 ,
          #time.sleep(11)  #pos 11
          #time.sleep(19) # pos 7-8
          
          pyautogui.mouseUp()
          pydirectinput.press('e') 
          fcount = fcount+1
          pressed = 'no' 
          old = 0
          i = 0 
          time_nr = 0

          directionfish = None
          print("Waiting for a new fish...")

      cv2.imshow('Computer Vision', src)

      print('FPS: {}'.format(1 / (time.time() - loop_time)))
      loop_time = time.time() 
      

      now = datetime.datetime.now()
      if now - last > datetime.timedelta(seconds=1):
        last = now
        time_nr += 1
        if time_nr > 80:
            pydirectinput.keyUp('a')  
            pydirectinput.keyUp('d') 
            pyautogui.mouseUp()
            print("fish not found after 80 seconds! breaking the loop!")
            break

      cv2.waitKey(1)
      if keyboard.is_pressed('q'):
          cv2.destroyAllWindows() 
          run = False



