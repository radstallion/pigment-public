import win32api
import time
import math

for i in range(5000):
    x = int(500+math.sin(math.pi*i/1000)*500)
    y = int(500+math.cos(i/100)*100)
    win32api.SetCursorPos((x,y))
    time.sleep(.01)
