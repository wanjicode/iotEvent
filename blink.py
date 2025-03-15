import RPi.GPIO as GPIO  # Import GPIO library
import time  # Import time module for delays

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering
LED_PIN = 17  # Define the GPIO pin for the LED

# Set up the LED pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

# Blink the LED in a loop
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
        print("LED ON")
        time.sleep(1)  # Wait for 1 second
        
        GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED off
        print("LED OFF")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    print("Exiting program")
    GPIO.cleanup()  # Reset GPIO settings before exiting

