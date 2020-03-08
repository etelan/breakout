#TODO: Wall collisions need to be dynamic
#TODO: Bounce, ball.py, needs to be dynamic

#Pygame library for games.
import pygame
from paddle import Paddle
from ball import Ball

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

#Make Ball
ball = Ball(white, 10, 10)
ball.rect.x = 300
ball.rect.y = 300

#Sprite list
all_sprites_list = pygame.sprite.Group()

#Add our sprites to the list
all_sprites_list.add(paddleA)
all_sprites_list.add(ball)

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


            #Start Paddle movement
            
            if event.key == pygame.K_a:
                paddleA.movement[0] = -1*paddleA.speed #it is moving left
            elif event.key == pygame.K_d:
                paddleA.movement[0] = 1*paddleA.speed #it is moving right

                                
        elif event.type == pygame.KEYUP:
            #End Paddle movement
            if event.key == pygame.K_a:
                paddleA.movement[0] = 0 #is is not moving left
            if event.key == pygame.K_d:
                paddleA.movement[0] = 0 #is is not moving right
            
        
    
    #Stop moving
        

    #Game Logic
    all_sprites_list.update()

    #Bounce Against Walls
    if ball.rect.x>=(width + 5):
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>height:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<5:
        ball.velocity[1] = -ball.velocity[1]
        
    #Bounce against the paddles
    if pygame.sprite.collide_mask(ball, paddleA):
      ball.bounce()
    

    #Drawing
    screen.fill(black) #Background
    all_sprites_list.draw(screen) #Sprites
    
    
    #always update everything
    paddleA.update()
    paddleA.checkbounds()
    pygame.display.flip() #update display
    clock.tick(60) #this code gives us our 60FPS.
    
