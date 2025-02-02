''' Author: Briana Bouchard
This script moves a stepper motor a set number of steps. 
'''  
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for the L298N motor driver
OUT1 = 12
OUT2 = 11
OUT3 = 13
OUT4 = 15

# Set the GPIO pins as output
GPIO.setup(OUT1, GPIO.OUT)
GPIO.setup(OUT2, GPIO.OUT)
GPIO.setup(OUT3, GPIO.OUT)
GPIO.setup(OUT4, GPIO.OUT)

# Set initial state of pins to low
GPIO.output(OUT1,GPIO.LOW)
GPIO.output(OUT2,GPIO.LOW)
GPIO.output(OUT3,GPIO.LOW)
GPIO.output(OUT4,GPIO.LOW)

# Sets number of steps to move
num_steps = 200

# Sets delay between steps
step_delay = 0.03

# Try-Except block asks program to complete try tasks until keyboard interrupt (CNTL-C)
try:
    while True:   
        current_step = 0
        
        for x in range(num_steps):
            if current_step == 0:
                GPIO.output(OUT1,GPIO.HIGH)
                GPIO.output(OUT2,GPIO.LOW)
                GPIO.output(OUT3,GPIO.HIGH)
                GPIO.output(OUT4,GPIO.LOW)
                time.sleep(step_delay)
                #print("step 0")
            elif current_step == 1:
                GPIO.output(OUT1,GPIO.LOW)
                GPIO.output(OUT2,GPIO.HIGH)
                GPIO.output(OUT3,GPIO.HIGH)
                GPIO.output(OUT4,GPIO.LOW)
                time.sleep(step_delay)
                #print("step 1")
            elif current_step == 2:
                GPIO.output(OUT1,GPIO.LOW)
                GPIO.output(OUT2,GPIO.HIGH)
                GPIO.output(OUT3,GPIO.LOW)
                GPIO.output(OUT4,GPIO.HIGH)
                time.sleep(step_delay)
            elif current_step == 3:
                GPIO.output(OUT1,GPIO.HIGH)
                GPIO.output(OUT2,GPIO.LOW)
                GPIO.output(OUT3,GPIO.LOW)
                GPIO.output(OUT4,GPIO.HIGH)
                time.sleep(step_delay)
            if current_step == 3:
                current_step = 0
                continue 
            current_step = current_step + 1
        GPIO.cleanup()
        break    
                    
except KeyboardInterrupt:
    GPIO.cleanup()

