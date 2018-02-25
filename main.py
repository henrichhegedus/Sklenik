from machine import Pin,PWM
import utimeimport machine
vlhkost_meranie=0
vlhkost={}
fan = PWM(Pin(15))pin_vlhkost = machine.PWM(machine.Pin(13))

def aktualny_cas():
  return(utime.mktime(utime.localtime()))
  def ventilator(cas):  fan.duty(1024)  time.sleep(cas)  fan.duty(0)def vlhkost_pody():
  global vlhkost_meranie
  vlhkost_meranie+=1
  data=open('data.txt',"a")  list=[]  adc = machine.ADC(0)  for i in range(10):    pin_vlhkost.duty(1024)    utime.sleep(1)    list.append((1024-adc.read())/480)
  pin_vlhkost.duty(0)
  average=sum(list[5:])/5
  vlhkost.update({vlhkost_meranie:[average,aktualny_cas()]})
  print(vlhkost)
  data.write(str(vlhkost))  data.close()
vlhkost_pody()

