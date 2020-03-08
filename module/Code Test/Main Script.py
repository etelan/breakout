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
moveleft = 0

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
            print("tick down")
            if event.key ==pygame.K_l: #press L to also quit
                running = False
                pygame.quit() #close the window


            #start movement
            if event.key == pygame.K_a:
                moveleft = 1 #it is moving left
                                
        elif event.type == pygame.KEYUP:
            #end movement
            if event.key == pygame.K_a:
                moveleft == 0 #is is not moving left
                
    
        #Movement
        if moveleft == 1:
            paddleA.moveLeft(5) #move left
            print("left")
        
    
        

    #Game Logic
    all_sprites_list.update()
    

    #Drawing
    screen.fill(black) #Background
    all_sprites_list.draw(screen) #Sprites
    
    
    #always update everything
    pygame.display.flip() #update display
    clock.tick(60) #this code gives us our 60FPS.
    
