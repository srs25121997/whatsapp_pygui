import pyautogui 
import time
from pynput import keyboard
from pynput.keyboard import Key, Listener 


print(pyautogui.size()) 
time.sleep(1)  

y=0
c = 0
x = 0
def on_press(key):  
    try:
        global y
        print(y)
        y=y+1
        if(y==1):
            global c
            global x
        print(key)
    
        if(key.char=='s'):
            pyautogui.moveTo(320, 30, duration = 1) 
            pyautogui.click(320, 30) 

            pyautogui.moveTo(200, 186, duration = 1) 
            pyautogui.scroll(-596+x)
            pyautogui.click(430, 190)
            pyautogui.moveTo(200, 186, duration = 0) 

            print("ender s or g")
        if(key.char=='g'):
            c=c+1
            pyautogui.click(200, 186)
            pyautogui.click(484, 737) 
            time.sleep(1)

            pyautogui.click(484, 666) 
            time.sleep(1)

            pyautogui.typewrite('invitation', interval=0)
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter')
            x = x-85
            print(c)
        elif(key.char=='l'):
            c=c+1
            x = x-85
            pyautogui.scroll(-85)
            print('not sending')
    except:
        print("Enter")
with Listener(on_press = on_press) as listener: 
                    
    listener.join() 
