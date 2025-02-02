import RPi.GPIO as GPIO
import time

# Assign GPIO pin numbers to variables

s0 = 13
s1 = 15
s2 = 16
s3 = 18
sig = 22 #labeled "out" on your board
cycles = 10

# Setup GPIO and pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(s0, GPIO.OUT)
GPIO.setup(s1, GPIO.OUT)
GPIO.setup(s2, GPIO.OUT)
GPIO.setup(s3, GPIO.OUT)
GPIO.setup(sig, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set frequency scaling
GPIO.output(s0, GPIO.HIGH)
GPIO.output(s1, GPIO.LOW)

def DetectColor():
    # Detect red values
    GPIO.output(s2, GPIO.LOW)
    GPIO.output(s3, GPIO.LOW)
    time.sleep(0.1)
    start_time = time.time()
    for count in range(cycles):
        GPIO.wait_for_edge(sig, GPIO.FALLING)
    duration = time.time() - start_time
    red = cycles / duration
    print("red value - ", red)

    # Detect blue values
    GPIO.output(s2, GPIO.LOW)
    GPIO.output(s3, GPIO.HIGH)
    time.sleep(0.1)
    start_time = time.time()
    for count in range(cycles):
        GPIO.wait_for_edge(sig, GPIO.FALLING)
    duration = time.time() - start_time
    blue = cycles / duration
    print("blue value - ", blue)

    # Detect green values
    GPIO.output(s2, GPIO.HIGH)
    GPIO.output(s3, GPIO.HIGH)
    time.sleep(0.1)
    start_time = time.time()
    for count in range(cycles):
        GPIO.wait_for_edge(sig, GPIO.FALLING)
    duration = time.time() - start_time
    green = cycles / duration
    print("green value - ", green)

try:
    while True:
        DetectColor()

except KeyboardInterrupt:
    GPIO.cleanup()