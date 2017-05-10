import RPi.GPIO as GPIO
import time
outports=[7,11,13,15]
rotat_pin=[[True,False,False,False],
           [True,True,False,False],
           [False,True,False,False],
           [False,True,True,False],
           [False,False,True,False],
           [False,False,True,True],
           [False,False,False,True],
           [True,False,False,True]]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outports,GPIO.OUT)
for j in range(10):    
    for i in range(8):
        GPIO.output(outports,rotat_pin[i])
        time.sleep(0.5)
        #GPIO.output(outports,[False,True,False,True])
        #time.sleep(1)
GPIO.cleanup()
