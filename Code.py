#import the necessary libraries
import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer  
 
# Search terms that you want to search from the twitter in the real time streaming 
TERM1= '#yes'
TERM2= ‘#bad’
# combine both the terms that has been defined to create a list of terms 
TERMS= ‘#yes,#bad’
 
# GPIO pin number of LED
LED1= 18
LED2=26
 # collect the secret tokens and the keys from the twitter developer application 
APP_KEY = ' XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX’
APP_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX’
OAUTH_TOKEN = ' XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
OAUTH_TOKEN_SECRET = ' XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#create a class that searches for the terms that been defined above  
class BlinkyStreamer1(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
#if term1 is found ie “yes” then LED1 should blink
                       if TERM1 in data[‘text’]:
                              print “LED1”
                              print 
                             GPIO.output(LED1, True)
                           Time.sleep(0.5)
                           GPIO.output(LED1, False)
#if term2 is found ie “bad” then LED2 should blink
                    elif TERM2 in data[‘text’]:
                             print “LED2”
                             print 
                             GPIO.output(LED2, True)
                           Time.sleep(0.5)
                           GPIO.output(LED2, False)
 
# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
 
# Create streamer that continuously  tracks for the terms and calls for the function 
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        Print “connected to twitter”
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()
