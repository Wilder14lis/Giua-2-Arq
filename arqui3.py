from machine import Pin
import utime
led1=pin(23,Pin.OUT)
led2=pin(21,pin.OUT)
led3=pin(19,Pin.OUT)
led4=pin(17,Pin.OUT)
led5=pin(0,Pin.OUT)
led6=pin(34,Pin.OUT)
led7=pin(35,Pin.OUT)
led8=pin(32,Pin.OUT)
led9=pin(33,Pin.OUT)
led10=pin(25,Pin.OUT)
todos = [led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]
def derecha():
    for elemento in todos:
        elemento.value(1)
        utime.sleep_ms(50)
        elemento.value(0)
        utime.sleep(0.05)
def izquierda():
    for elemento in reversed(todos):
    elemento.value(1)
    utime.sleep_ms(0.05)
    elemento.value(0)
    utime.sleep(0.05)
while True:
    derecha()
    izquierda()