#Pygame library for games.
import pygame

#Initialize the pygame window
pygame.init()
width = 350
height = 200

#Set the display as variable screen.
screen = pygame.display.set_mode((width, height ))

#Set Caption
pygame.display.set_caption("This Is A Caption")

#Set Background Colour
red = [255,0,0]
screen.fill(red)
pygame.display.update()

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
            
    
