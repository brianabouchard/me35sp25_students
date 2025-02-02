#Author: Darya Clark

import RPi.GPIO as GPIO
import time

# GPIO pins for the ultrasonic sensor
# See wiring diagram in /WiringDiagrams/Ultrasonic.png
GPIO_TRIGGER = 40
GPIO_ECHO = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def measure_distance():
    # Set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    start_time = time.time()
    stop_time = time.time()

    # Save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    # Save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    # Time difference between start and arrival
    time_elapsed = stop_time - start_time
    print(time_elapsed)

    # Speed of sound in air (343 meters per second) and 100 for conversion to centimeters
    distance_cm = round((time_elapsed * 34300) / 2, 2)

    print(distance_cm)
    
    time.sleep(0.1)

    return distance_cm

try:
    while True:
        measure_distance()

except KeyboardInterrupt:
    GPIO.cleanup()
