from pygame import mixer
import menu
import splash
import classic

#Set Up Current Directory
import os
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
