from machine import Pin
import time

led=Pin( 3 ,Pin.OUT)
button_pin = Pin( 7 , Pin.IN, Pin.PULL_UP)


bt = 0
while True:
# Check if the button is pressed (LOW)
    if (button_pin.value() == 0 and bt == 0):
        print("Button Pressed!")
        # Debounce delay to prevent multiple readings
        led.value(1) # LED 동작
        time.sleep(0.5)
        bt = 1

    elif (button_pin.value() == 0 and bt == 1):
        print("Button OFF!")
        led.value(0)
        time.sleep(0.5)
        bt = 0
    time.sleep(0.01)  