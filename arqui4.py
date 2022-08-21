from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
leda=pin(23,pin.OUT)
ledb=pin(21,pin.OUT)
ledc=pin(19,pin.OUT)
ledd=pin(17,pin.OUT)
lede=pin(0,pin.OUT)
ledf=pin(34,pin.OUT)
ledg=pin(35,pin.OUT)
ledh=pin(32,pin.OUT)
ledi=pin(33,pin.OUT)
ledj=pin(25,pin.OUT)
ledk=[leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi,ledj]
def derecha ():
    for i in ledt:
        for j in range (2):
            i.value(not i,value())
            pausam(150)
def izquierda():
    for i in reversed(left):
        for j in range (2):
            i.value(not i.value())
            pausam(150)
while True:
    derecha()
    izquierda()