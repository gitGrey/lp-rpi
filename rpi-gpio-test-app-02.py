#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

import RPi.GPIO as GPIO

class port:
     def __init__(self, name, gpioNum, pinNum):
          # GPIO-Name ( the Port Name as string)
          # Broadcom-Chip-GPIO-Name  
          #      --> GPIO.setmode(GPIO.BCM)
          # Raspberry-Extension-Port-Connector-Pin-Number
          #      --> GPIO.setmode(GPIO.BOARD)
          self.name = name
          self.gpioNum = gpioNum
          self.pinNum = pinNum

global portRange

portRange=[]

portX=port("GPIO-4", 4, 7)
portRange.append(portX)

portX=port("GPIO-14", 14, 8)
portRange.append(portX)

portX=port("GPIO-18", 18, 12)
portRange.append(portX)

portX=port("GPIO-22", 22, 15)
portRange.append(portX)

portX=port("GPIO-23", 23, 16)
portRange.append(portX)

portX=port("GPIO-24", 24, 18)
portRange.append(portX)

portX=port("GPIO-25", 25, 22)
portRange.append(portX)

portX=port("GPIO-27", 27, 13)
portRange.append(portX)

gpio_start = 1
gpio_end = 27

def portsOutputTest():
     GPIO.setmode(GPIO.BCM)

     for x in range (gpio_start, gpio_end):
          GPIO.setup(x, GPIO.OUT)

     while True:
              
          for y in range (gpio_start, gpio_end):
               GPIO.output(y, True)
               print('on ' %  y)
          time.sleep(0.5)
    
          for z in range (gpio_start, gpio_end):
               GPIO.output(z, False)
               print('off ' % z)
          time.sleep(0.5)


# *******************************************************
# *******************************************************
# Program starts here
# *******************************************************
# *******************************************************

if __name__ == '__main__':
     
     appname=os.path.basename(__file__)     # get this script name

     print("this script need root-rights")
     print("run like: sudo ./%s" % appname)

     pfad=os.path.dirname(os.path.realpath(__file__))   # pfad wo dieses script läuft
    
     print("for this test we have a button/taster connected")
     print("on th eport of interest to GND")
     print("")

     # RPi.GPIO Layout verwenden (wie Pin-Nummern am Stecker)
     GPIO.setmode(GPIO.BOARD)
     

     for port in portRange:
            
          if port.gpioNum == 23:      
               print("Port")
               print("  Name  : %s" % port.name)
               print("  GPIO# : %s" % port.gpioNum)
               print("  Pin#  : %s" % port.pinNum)
               print("")
          
               GPIO.setup(port.pinNum, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
               # GPIO lesen
               #if GPIO.input(18) == GPIO.HIGH:

               maxTests=5
              
               for i in range(1,maxTests+1): 
                    print("Test %d/%d" % (i,maxTests))
                    print("Waiting for button to be pressed")
                    GPIO.wait_for_edge(port.pinNum, GPIO.FALLING)
                    #GPIO.wait_for_edge(BUTTON_CHANNEL, GPIO.RISING)
                    print("button press successfully received") 
                    print("")
                    print("")
                    time.sleep(0.5)

     GPIO.cleanup()

     print("")
     print("")
     print("Ready")




