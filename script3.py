import webiopi
import RPi.GPIO as GPIO
import time

GPIO = webiopi.GPIO
comida = 2
agua_in = 4
agua_out = 17
global timer_comida, timer_agua_in, timer_agua_out
timer_comida = 0
timer_agua_in = 0
timer_agua_out = 0
slider = 26
GPIO.setFunction(slider, GPIO.PWM)

def loop():
    global timer_comida, timer_agua_in, timer_agua_out
    if(timer_comida > 0):
        GPIO.digitalWrite(comida, GPIO.HIGH)     # set the pin LOW
        timer_comida = timer_comida - 1                         # counting down to zero
    else:
        GPIO.digitalWrite(comida, GPIO.LOW)    # set the pin HIGH
    webiopi.sleep(1)

    if(timer_agua_out > 0):
        GPIO.digitalWrite(agua_out, GPIO.HIGH)     # set the pin LOW
        timer_agua_out = timer_agua_out - 1                         # counting down to zero
    else:
        GPIO.digitalWrite(agua_out, GPIO.LOW)    # set the pin HIGH
    webiopi.sleep(1)
	
    if((timer_agua_in > 0) and (timer_agua_out == 0)):
        GPIO.digitalWrite(agua_in, GPIO.HIGH)     # set the pin LOW
        timer_agua_in = timer_agua_in - 1                         # counting down to zero
    else:
        GPIO.digitalWrite(agua_in, GPIO.LOW)    # set the pin HIGH
    webiopi.sleep(1)

@webiopi.macro
def timer_30g():
    global timer_comida
    timer_comida = 2    # start the timer
	
@webiopi.macro
def timer_50g():
    global timer_comida
    timer_comida = 4    # start the timer
	
@webiopi.macro
def timer_80g():
    global timer_comida
    timer_comida = 6    # start the timer
	
@webiopi.macro
def timer_water():
    global timer_agua_in, timer_agua_out
    timer_agua_out = 5
    timer_agua_in = 3    # start the timer
	
	
	
	
	
