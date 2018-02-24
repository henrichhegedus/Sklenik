from machine import Pin,PWM
import machine
import time
fan = PWM(Pin(15))
pin_vlhkost = machine.PWM(machine.Pin(13))
def ventilator(cas):
  fan.duty(1024)
  time.sleep(cas)
  fan.duty(0)

def vlhkost_pody():
  list=[]
  adc = machine.ADC(0)
  for i in range(10):
    pin_vlhkost.duty(1024)
    time.sleep(1)
    list.append((1024-adc.read())/480)
  print (sum(list[5:])/5)
  pin_vlhkost.duty(0)
  

vlhkost_pody()

