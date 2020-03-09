
#import pygame and os
from pygame import mixer
import os

#import modules
import menu
import splash

#Set Up Current Directory
current_path = str(__file__).replace("\BREAKOUT.py", "")
os.chdir(current_path)
print(os.getcwd())
print(current_path)

#Sound Test
mixer.init()
mixer.music.load("Ctrim.wav")
mixer.music.play()

#Play Splash
splash.main()

#Main Menu
menu.main()
 
