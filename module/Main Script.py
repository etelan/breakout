#TODO: Wall collisions need to be dynamic
#TODO: Bounce, ball.py, needs to be dynamic

#Imports.
import pygame
import splash
import menu
from paddle import Paddle
from ball import Ball
from brick import Brick

#Splash screen
splash.main()

#Menu screen
menu.main()


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
            

        #Key Down Event
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_l: #press L to also quit
                running = False
                


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
        lives -= 1
        print(lives)
        if lives <= 0:
            font = pygame.font.Font(None, 74)
            text = font.render("YOU LOSE", 1, white) # game over
            screen.blit(text, (250,300))
            font = pygame.font.Font(None, 34)
            text = font.render("Points: " + str(score), 1, white) # Points
            screen.blit(text, (250,400)) #draw points
            pygame.display.flip()
            pygame.time.wait(3000)
            
            running = False #quit the game
        
    if ball.rect.y<5:
        ball.velocity[1] = -ball.velocity[1]
        
    #Bounce against the paddles
    if pygame.sprite.collide_mask(ball, paddleA):
        ball.rect.y -= 10
        ball.bounce()

    #Bounce against bricks
    brick_current_collides = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_current_collides:
        score += 1
        brick.kill()
        ball.bounce()
        if len(all_bricks)==0: #If there are no bricks left, you win
            font = pygame.font.Font(None, 65)
            text = font.render("YOU WIN", 1, white)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = 0  #stop the game
    

    #Drawing
    screen.fill(black) #Background
    all_sprites_list.draw(screen) #Sprites

    #Drawing Text
    font = pygame.font.Font(None, 34)
    text = font.render("Points: " + str(score), 1, white)
    screen.blit(text, (20,10)) #draw points
    text = font.render("Lives " + str(lives), 1, white)
    screen.blit(text, (650, 10)) #draw lives
    
    
    #always update everything
    paddleA.update()
    paddleA.checkbounds()
    pygame.display.flip() #update display
    clock.tick(60) #this code gives us our 60FPS.

#Out of Main Loop
pygame.quit() #close the window
    
