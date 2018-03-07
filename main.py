from machine import Pin
import utime,machine,dht
sensor=dht.DHT11(machine.Pin(2))
meranie=0
fan = Pin(15, Pin.OUT)
pin_vlhkost = Pin(13, Pin.OUT)
pump=Pin(0, Pin.OUT)
zatvorit=Pin(4, Pin.OUT)
otvorit=Pin(5, Pin.OUT)

# Definovanie funkcie vetrania. Funkcia otvori ventil ak je vlhkost vacsia alebo rovna 70%. Otvori vetranie na 20s a pusti ventilator
# ventilator sa vypne tesne pred tym ako sa zatvori vetranie
def vetranie(value):
  if value>=70:
    otvorit.on()
    utime.sleep(0.5)
    otvorit.off()
    fan.on()
    utime.sleep(20)
    fan.off()
    zatvorit.on()
    utime.sleep(0.5)
    zatvorit.off()
    
# Ked je tato funkcia vyvolana tak vrati aktualny cas
def aktualny_cas():  
  return(utime.mktime(utime.localtime()))  

# Funkcia zavlaha bere jeden argument vlhkost a podla toho ci je menej alebo viac ako 45 zapne alebo necha vypnute zalievanie.
# Ak zalievanie zapne tak bude pustene na 10s
def zavlaha(vlhkost):
  if vlhkost<=45:
    pump.on()
    utime.sleep(10)
    pump.off()
  
# Funkcia vlhkost_a_teplota zapise do textoveho suboru data.txt aktualnu vlhkost a teplotu vzduchu aktualny cas a cislo merania.
# Navyse tato funkcia vrati vlhkost ktora je pouzita na urcenie toho ci sa bude vetrat alebo nie
def vlhkost_a_teplota():
  sensor.measure()
  data=open('data.txt',"a")
  data.write(str({meranie:[sensor.humidity(),sensor.temperature(),aktualny_cas()]}))
  data.close()
  return(sensor.humidity())
# Funkcia vlhkost_pody odmeria 10x za sebou vlhkost pody kazde meranie zapise do listu list potom z poslednych piatich merani
# je vypocitany priemer ktoreho hodnota je ulozena do premennej average. Po 10 meraniach sa privod prudu do senzora vypne aby
# nekorodoval zbytocne. Priemer nameranych hodnot je zapisany do textoveho suboru data.txt aj s cislom merania a aktualnym casom
# Taktiez funkcia vrati vlhkost pody v percentach ktora je vyuzivana na urcenie toho ci sa bude zavlazovat alebo nie
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
# Tento loop zaruci to ze kazdu hodinu prebehne jedno meranie a sklenik skontroluje ci nie je potrebne zalievat alebo vetrat
while 1==1:
  meranie+=1
  vetranie(vlhkost_a_teplota())
  zavlaha(vlhkost_pody())
  utime.sleep(3600)

