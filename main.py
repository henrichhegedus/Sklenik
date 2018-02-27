from machine import Pin,PWM
import utime,machine,dht
sensor=dht.DHT11(machine.Pin(2))
meranie=0
vlhkost={}
vlhkost_zem={}
vzduch_hodnoty={}
fan = PWM(Pin(15))
pin_vlhkost = machine.PWM(machine.Pin(13))



def aktualny_cas():  
  return(utime.mktime(utime.localtime()))  
 
 
 
def ventilator(cas):
  fan.duty(1024)
  utime.sleep(cas)
  fan.duty(0)
  
  
  
def vlhkost_a_teplota():
  sensor.measure()
  data=open('data.txt',"a")
  data.write("{vzduch_hodnoty_%d:" %meranie+str([sensor.humidity(),sensor.temperature(),aktualny_cas()])+"}")
  data.close()

def cas():
  if sensor.humidity()>=70:
    return (10)
  else:
    return (0)
 
 
def vlhkost_pody():
  data=open('data.txt',"a")
  list=[]
  adc = machine.ADC(0)
  for i in range(10):
    pin_vlhkost.duty(1024)
    utime.sleep(0.2)
    list.append((1024-adc.read())/480)
  pin_vlhkost.duty(0)
  average=sum(list[5:])/5
  
  data.write("{vlhkost_pody_%d:" %meranie+str([average,aktualny_cas()])+"}")
  data.close()

for i in range(10):
  meranie+=1
  vlhkost_pody()
  vlhkost_a_teplota()
  ventilator(cas())
  utime.sleep(30)



  

