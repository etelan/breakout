#TODO: Wall collisions need to be dynamic
#TODO: Bounce, ball.py, needs to be dynamic

#Imports.
import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

#Initialise Game Engine
pygame.init()

#Set Colours
red = [255,0,0]
white = [255,255,255]
black = [0,0,0]
green = [0,255,0]

#score and lives
score = 0
lives = 3

#Set the pygame window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")

#Keys down
adown = 0
ddown = 0

#Make Paddle
paddleA = Paddle(white,100,10)
paddleA.rect.x = 300
paddleA.rect.y = 540

#Make Ball
ball = Ball(white, 10, 10)
ball.rect.x = 300
ball.rect.y = 500

#Sprite list
all_sprites_list = pygame.sprite.Group()

#Make Bricks
all_bricks = pygame.sprite.Group()

rows = 8
bricks = 8
row_gap = 20

for i in range(rows - 1): #rows
    row_gap += 40
    for i in range(bricks - 1):
        brick = Brick(red,80,30)
        brick.rect.x = 60 + i*100 #this spaces them out along a line
        brick.rect.y = row_gap
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    



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
        
        #Quit Event
        if event.type == pygame.QUIT: #press quit button
            running = False
            pygame.quit() #close the window

        #Key Down Event
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_l: #press L to also quit
                running = False
                pygame.quit() #close the window


            #Start Paddle movement
            if event.key == pygame.K_a:
                adown = 1 #A key is down
            elif event.key == pygame.K_d:
                ddown = 1 #D key is down

        #Key Up Event                        
        elif event.type == pygame.KEYUP:
            #End Paddle movement
            if event.key == pygame.K_a:
                adown = 0 #A key is up
            if event.key == pygame.K_d:
                ddown = 0 #D key is up
            
        
    
    #Movement Code Paddle
    if adown == 1:
        paddleA.movement[0] = -1*paddleA.speed #it is moving left
    if ddown == 1:
        paddleA.movement[0] = 1*paddleA.speed #it is moving right
    
    #Stopping code Padde
    if (adown == 0) and (ddown == 0):
        print("Nothing is down")
        paddleA.movement[0] = 0

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

    #Bounce against bricks
    brick_current_collides = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_current_collides:
        score += 1
        brick.kill()
        ball.bounce()
    

    #Drawing
    screen.fill(black) #Background
    all_sprites_list.draw(screen) #Sprites
    
    
    #always update everything
    paddleA.update()
    paddleA.checkbounds()
    pygame.display.flip() #update display
    clock.tick(60) #this code gives us our 60FPS.
    
