import RPi.GPIO as GPIO 
import time

# define the gpio
all_pin = [11,12,13,15]
buzzer = 12 # GPIO.1 (pin 12)
led_red = 11 # GPIO.0 (pin 11)
led_yellow = 13 # GPIO.2 (pin 13)
led_green = 15 # GPIO.3 (pin 15)

def setup():
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BOARD) 
   GPIO.setup(all_pin, GPIO.OUT) 
   GPIO.output(all_pin, GPIO.HIGH) 

# match with person in DB
def match_person_twinkle():
   print('Match with person in DB')
   GPIO.output(led_red, GPIO.LOW)
   GPIO.output(led_yellow, GPIO.LOW)
   GPIO.output(buzzer, GPIO.HIGH)
   while True:    
     GPIO.output(led_green, GPIO.LOW) # green led on
     time.sleep(0.5)

     GPIO.output(led_green, GPIO.HIGH) # led off
     time.sleep(0.5) 

# match with person in DB not twinkle
def match_person():
   print('Match with person in DB')
   GPIO.output(led_red, GPIO.LOW)
   GPIO.output(led_yellow, GPIO.LOW)
  
   GPIO.output(led_green, GPIO.HIGH) # led off
   GPIO.output(buzzer, GPIO.LOW)

# missmatch with person in DB
def missmatch_person_twinkle():
   print('Missmatch with person in DB')
   GPIO.output(led_green, GPIO.LOW)
   GPIO.output(led_yellow, GPIO.HIGH)
   while True:    
     GPIO.output(led_red, GPIO.LOW) # led on
     GPIO.output(buzzer, GPIO.LOW) 
     time.sleep(0.5)

     GPIO.output(led_red, GPIO.HIGH) # led off
     GPIO.output(buzzer, GPIO.HIGH)
     time.sleep(0.5)
 
# missmatch with person in DB not twinkle
def missmatch_person():
   print('Missmatch with person in DB')
   GPIO.output(led_green, GPIO.LOW)
   GPIO.output(led_yellow, GPIO.LOW)
   GPIO.output(buzzer, GPIO.HIGH)
   
   GPIO.output(led_red, GPIO.HIGH) # led on
    



def destroy():
    GPIO.output(LedPin, GPIO.HIGH) # led off
    GPIO.cleanup() 

'''
if __name__ == '__main__': 
    setup()
try:
    match_person()
except KeyboardInterrupt: 
    destroy()
'''
