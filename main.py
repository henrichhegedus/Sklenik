from machine import Pin
import utime,machine,dht
sensor=dht.DHT11(machine.Pin(2))
meranie=0
fan = Pin(15, Pin.OUT)
pin_vlhkost = Pin(13, Pin.OUT)
pump=Pin(0, Pin.OUT)
zatvorit=Pin(4, Pin.OUT)
otvorit=Pin(5, Pin.OUT)

def vetranie(value):
  if value>=70:
    otvorit.on()
    utime.sleep(2)
    otvorit.off()
    utime.sleep(1)
    fan.on()
    utime.sleep(20)
    fan.off()
    utime.sleep(1)
    zatvorit.on()
    utime.sleep(2)
    zatvorit.off()
    

def aktualny_cas():  
  return(utime.mktime(utime.localtime()))  
  
def zavlaha(vlhkost):
  if vlhkost<=45:
    pump.on()
    utime.sleep(10)
    pump.off()
  
  

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
    pin_vlhkost.on()
    utime.sleep(0.2)
    list.append((1024-adc.read())/315)
  pin_vlhkost.off()
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

