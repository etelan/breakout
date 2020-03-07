import pygame
#This allows us to use the pygame library.

#Initialize the pygame window
pygame.init()
width = 350
height = 200

#Set the display
pygame.display.set_mode((width, height ))

#Tell the game to run
running = True

#While it is running, do something else.
while(running):
    #Get all the user events at each frame
    for event in pygame.event.get():
        #If the event is a quit, quit.
        if event.type == pygame.QUIT:
            #Set running to false, as we want it to quit.
            running = False
    
