#TODO: Add character
#TODO: Add blocks to hit with ball.

#Pygame library for games.
import pygame

#Set the pygame window
pygame.init()
width = 350
height = 200

#Set the display as variable screen.
screen = pygame.display.set_mode((width, height ))

#Set Caption
pygame.display.set_caption("Breakout")

#Set Background Colours
red = [255,0,0]
white = [255,255,255]
black = [0,0,0]

#Set our colour and update
screen.fill(black)
pygame.display.update()

 

#Tell the game to run
running = True

#Main Loop
while(running):
    
    #Get all the user events at each frame
    for event in pygame.event.get():
        
        #If the event is a quit, quit.
        if event.type == pygame.QUIT:
            #Set running to false, as we want it to quit.
            running = False
            pygame.quit()

    #Detecting Keys
    pressedKeys = pygame.key.get_pressed()

    #If statement based on keys.
    #Left
    if pressedKeys[pygame.K_LEFT] or pressedKeys[ord('a')]:
        print("left detected")
    #Right
    if pressedKeys[pygame.K_RIGHT] or pressedKeys[ord('d')]:
        print("right detected")
            
    
