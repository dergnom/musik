#!/usr/bin/python3

import RPi.GPIO as GPIO
import time as time
import threading
import multiprocessing
from os import system


SWITCH_PIN = 4
PIN2 = 22
PIN3 = 24
OFF_PIN = 6
PLUS_PIN = 17
MINUS_PIN = 27

#musicFile = '/home/thomas/Python/Media/Bell.mp3'
musicFile = '/home/thomas/Python/Media/PippiLangstrumpf.mp3'
musicFile2 = '/home/thomas/Python/Media/lied2.mp3'
musicFile3 = '/home/thomas/Python/Media/fabian.mp3'

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN)
GPIO.setup(OFF_PIN, GPIO.IN)
GPIO.setup(PLUS_PIN, GPIO.IN)
GPIO.setup(MINUS_PIN, GPIO.IN)
GPIO.setup(PIN2, GPIO.IN)
GPIO.setup(PIN3, GPIO.IN)

def playSound(file):
    cmd = '/usr/bin/audacious -H ' + file
    print('playSound: ',cmd)
    rtrn = system(cmd)
    print('playSound: ',rtrn)


musicProcess = multiprocessing.Process(target=playSound, args=(musicFile,))

while True:
    bool(GPIO.input(SWITCH_PIN))

    if bool(GPIO.input(OFF_PIN)):
        print("Aus Schalter gedrückt")
        system("/usr/bin/audacious -H -s -q")
            
        time.sleep(0.1)
        while bool(GPIO.input(OFF_PIN)):
            time.sleep(0.1)
        else:
            print("Aus Schalter losgelassen")
            #warten, dass sich der Schalter beruhigt:
            time.sleep(0.3)

    if bool(GPIO.input(PLUS_PIN)):
        print("Plus Schalter gedrückt")
        system("/usr/bin/pactl -- set-sink-volume alsa_output.platform-bcm2835_audio.stereo-fallback +10%")
        time.sleep(0.1)
        while bool(GPIO.input(PLUS_PIN)):
            time.sleep(0.1)
        else:
            print("Plus Schalter losgelassen")
            #warten, dass sich der Schalter beruhigt:
            time.sleep(0.3)

    if bool(GPIO.input(MINUS_PIN)):
        print("Minus Schalter gedrückt")
        system("/usr/bin/pactl -- set-sink-volume alsa_output.platform-bcm2835_audio.stereo-fallback -10%")
        time.sleep(0.1)
        while bool(GPIO.input(MINUS_PIN)):
            time.sleep(0.1)
        else:
            print("Minus Schalter losgelassen")
            #warten, dass sich der Schalter beruhigt:
            time.sleep(0.3)



    if bool(GPIO.input(SWITCH_PIN)):
        print("Schalter gedrückt")

        if musicProcess.is_alive():
            musicProcess.terminate()
            musicProcess.join()
            musicProcess.close()
            
        musicProcess = multiprocessing.Process(target=playSound, args=(musicFile,))
        musicProcess.start()        
        
        while bool(GPIO.input(SWITCH_PIN)):
            time.sleep(0.1)
        else:
            print("Schalter losgelassen")
            #warten, dass sich der Schalter beruhigt:
            time.sleep(0.3)


    if bool(GPIO.input(PIN2)):
        print("PIN2 gedrückt")

        if musicProcess.is_alive():
            musicProcess.terminate()
            musicProcess.join()
            musicProcess.close()
            
        musicProcess = multiprocessing.Process(target=playSound, args=(musicFile2,))
        musicProcess.start()        
        
        while bool(GPIO.input(SWITCH_PIN)):
            time.sleep(0.1)
        else:
            print("PIN2 losgelassen")
            #warten, dass sich der Schalter beruhigt:
            time.sleep(0.3)


    if bool(GPIO.input(PIN3)):
        print("PIN3 gedrückt")

        if musicProcess.is_alive():
            musicProcess.terminate()
            musicProcess.join()
            musicProcess.close()
            
        musicProcess = multiprocessing.Process(target=playSound, args=(musicFile3,))
        musicProcess.start()        
        
        while bool(GPIO.input(SWITCH_PIN)):
            time.sleep(0.1)
        else:
            print("PIN3 losgelassen")
            #warten, dass sich der Schalter beruhigt:
            time.sleep(0.3)


    
    else:
        time.sleep(0.1)
