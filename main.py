from machine import Pin,PWM
import utime,machine,dht
sensor=dht.DHT11(machine.Pin(2))
meranie=0
fan = machine.PWM(machine.Pin(15))
pin_vlhkost = machine.PWM(machine.Pin(13))
pump=machine.PWM(machine.Pin(0))
zatvorit=machine.PWM(machine.Pin(4))
otvorit=machine.PWM(machine.Pin(5))

def vetranie(value):
  if value>=93:
    otvorit.duty(1024)
    utime.sleep(2)
    otvorit.duty(0)
    utime.sleep(1)
    fan.duty(1024)
    utime.sleep(20)
    fan.duty(0)
    utime.sleep(1)
    zatvorit.duty(1024)
    utime.sleep(2)
    zatvorit.duty(0)
    

def aktualny_cas():  
  return(utime.mktime(utime.localtime()))  
  
def zavlaha(vlhkost):
  if vlhkost<=45:
    print("pumpa")
    #pump.duty(1024)
    utime.sleep(10)
    pump.duty(0)
  
  

def vlhkost_a_teplota():
  sensor.measure()
  data=open('data.txt',"a")
  data.write(str({meranie:[sensor.humidity(),sensor.temperature(),aktualny_cas()]}))
  data.close()
  return(sensor.humidity())
 
def vlhkost_pody():
  data=open('data.txt',"a")
  list=[]
  adc = machine.ADC(0)
  for i in range(10):
    pin_vlhkost.duty(1024)
    utime.sleep(0.2)
    list.append((1024-adc.read())/315)
  pin_vlhkost.duty(0)
  average=sum(list[5:])/5
  data.write(str({meranie:[average*100,aktualny_cas()]}))
  data.close()
  print (average)
  return (average*100)

while 1==1:
  meranie+=1
  vetranie(vlhkost_a_teplota())
  zavlaha(vlhkost_pody())
  utime.sleep(3600)

