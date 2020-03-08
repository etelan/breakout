#Pygame library for games.
import pygame
from paddle import Paddle

#Initialise Game Engine
pygame.init()

#Set Colours
red = [255,0,0]
white = [255,255,255]
black = [0,0,0]
green = [0,255,0]

#Set the pygame window
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")

#Make Paddle
paddleA = Paddle(white,100,10)
paddleA.rect.x = 300
paddleA.rect.y = 360

#Sprite list
all_sprites_list = pygame.sprite.Group()

#Add our sprites to the list
all_sprites_list.add(paddleA)

#Tell the game to run
running = True

#Set our clock

clock = pygame.time.Clock()       

#Main Loop                      
while(running):

    #Main Event Loop
    for event in pygame.event.get():
        
        #Quit.
        if event.type == pygame.QUIT: #press quit button
            running = False
            pygame.quit() #close the window
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_l: #press L to also quit
                running = False
                pygame.quit() #close the window


        #Keys Held
        pressedKeys = pygame.key.get_pressed()
    
        #Keys Held Code
        #Left
        if pressedKeys[pygame.K_LEFT] or pressedKeys[ord('a')]:
            print("left detected")
            paddleA.moveLeft(5)
        #Right
        if pressedKeys[pygame.K_RIGHT] or pressedKeys[ord('d')]:
            print("right detected")
            paddleA.moveRight(5)
    
        

    #Game Logic
    all_sprites_list.update()
    

    #Drawing
    screen.fill(black) #Background
    all_sprites_list.draw(screen) #Sprites
    
    
    #always update everything
    pygame.display.flip() #update display
    clock.tick(60) #this code gives us our 60FPS.
    
