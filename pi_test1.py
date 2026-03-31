from time import sleep
from machine import Pin
#create LED object from pin2,Set Pin2 to output
led1=Pin(5,Pin.OUT)
led2=Pin(9,Pin.OUT)



while True:

    n= input()
    if n == '1':
        print('RED LED ON')
        led1.value(1)
        led2.value(0)
    elif n == '2':
        print('BLUE LED ON')
        led1.value(0)
        led2.value(1)
    elif n == '3':
        print('ALL LED ON')
        led1.value(1)
        led2.value(1)
    elif n == '4':
        print('ALL LED OFF')
        led1.value(0)
        led2.value(0)
