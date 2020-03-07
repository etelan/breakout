#TODO: Detect left and right keys <-
#TODO: Add character
#TODO: Add blocks to hit with ball.

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
white = [255,255,255]
screen.fill(white)
pygame.display.update()

#Tell the game to run
running = True

#Main Loop
while(running):
    
    #Get all the user events at each frame
    for event in pygame.event.get():

        #Key presses.
        if event.type == pygame.KEYDOWN:
            
            #Left
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print("left detected")
            #Right
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print("right detected")
        
        
        #If the event is a quit, quit.
        if event.type == pygame.QUIT:
            #Set running to false, as we want it to quit.
            running = False
            pygame.quit()
    
