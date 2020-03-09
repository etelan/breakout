def main():

#IMPORTING
    import pygame
    from pygame import mixer
    from paddle import Paddle
    from ball import Ball
    from brick import Brick

#FILE HANDLING
    #The Settings
    try: #Read The settings
        f = open("settings.txt", "r")
        lines=f.readlines()
        #Set the variables
        paddle_speed = int(lines[1])
        sound = int(lines[3])
        #Close the file
        f.close()
        
    #No File    
    except FileNotFoundError: #If there is no file, then we will have to make one.
        f = open("settings.txt", "w+")
        #Default Values
        f.write("[Paddle Speed]\n5" )
        f.write("\n[Sound]\0" )
        paddle_speed = int(5)
        sound = 0
        #Close the file
        f.close()

#INITIALIZE

    #Initialise Game Engine
    pygame.init()

    #Initialize sound
    mixer.init()
    #Notes
    E = "Etrim.wav"
    C = "Ctrim.wav"


    #Set Colours
    red = [255,0,0]
    white = [255,255,255]
    black = [0,0,0]
    green = [0,255,0]
    orange = [255,165,0]

    #score and lives
    score = 0
    lives = 5

    #Set the pygame window
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Breakout")

    #Keys down
    adown = 0
    ddown = 0

#CREATE OBJECTS

    #Make Paddle
    paddleA = Paddle(white,100,10, paddle_speed)
    paddleA.rect.x = 300
    paddleA.rect.y = 540

#!  #Make Fake Ball
    fake_ball = Paddle(white,10,10, paddle_speed)
    fake_ball.rect.x = 350
    fake_ball.rect.y = 520

#!  #Does the real ball exist yet?
    real_deployed = False
    

    #Sprite list
    all_sprites_list = pygame.sprite.Group()

    #Make Bricks Group
    all_bricks = pygame.sprite.Group()

    
    #Lay Bricks
    rows = 8
    bricks = 7
    row_gap = 20

    for i in range(rows): #rows
        row_gap += 40
        for i in range(bricks):
            brick = Brick(red,80,30)
            brick.rect.x = 60 + i*100 #this spaces them out along a line
            brick.rect.y = row_gap
            all_sprites_list.add(brick)
            all_bricks.add(brick)

    #Add our sprites to the list
    all_sprites_list.add(paddleA)
    all_sprites_list.add(fake_ball)

#RUNNING VARIABLES

    #Tell the game to run
    running = True

    #Set our clock
    clock = pygame.time.Clock()


#USER EVENTS

    #Main Loop                      
    while(running): 

        #Main Event Loop
        for event in pygame.event.get():
            
            #Quit Event
            if event.type == pygame.QUIT: #press quit button
                pygame.quit() #close the window
                

        #Key Down Event
                
            #Quit Event
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_l: #press L to also quit
                    running = False

#!              #Make Real Ball
                if real_deployed == False: #Then deploy the ball.
                    if event.key ==pygame.K_SPACE: #Switch out for real ball.

                        

                        #Grab the old balls position.
                        fake_y = fake_ball.rect.y
                        fake_x = fake_ball.rect.x

                        #Kill the old ball.
                        fake_ball.kill()

                        #Make the new ball and switch it.
                        ball = Ball(white, 10, 10)
                        ball.rect.x = fake_x
                        ball.rect.y = fake_y
                        all_sprites_list.add(ball)
                        real_deployed = True
                    


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
                
            
        
#!      #Movement Code Paddle and Fake Ball
        if adown == 1:
            paddleA.movement[0] = -1*paddleA.speed #it is moving left
            fake_ball.movement[0] = -1*paddleA.speed
        if ddown == 1:
            paddleA.movement[0] = 1*paddleA.speed
            fake_ball.movement[0] = 1*paddleA.speed #it is moving right

        
        
        #Stopping code Paddle
        if (adown == 0) and (ddown == 0):
            fake_ball.movement[0] = 0
            paddleA.movement[0] = 0


#BOUNCING

#!      #Is the ball deployed?
        if real_deployed == True:
            #Bounce Against Walls
            if ball.rect.y<5: #Upper Wall
                ball.velocity[1] = -ball.velocity[1]
            elif ball.rect.x>=(width - 5): #Right Wall
                ball.velocity[0] = -ball.velocity[0]
            elif ball.rect.x<=0: #Left Wall
                ball.velocity[0] = -ball.velocity[0]
            elif ball.rect.y>height: #Wall behind paddle
#!              Kill The Ball
                ball.kill()

                #Update Screen Colour
                screen.fill(orange) #Background Orange
                all_sprites_list.draw(screen)

                #Draw Warning
                font = pygame.font.Font(None, 72)
                text = font.render("ALERT! LIFE LOST, RESUMING...", 1, black)
                screen.blit(text, (10,paddleA.rect.y - 100)) #draw lives
                print("Drew Warning")

                #Draw the lives
                font = pygame.font.Font(None, 34)
                text = font.render("Lives " + str(lives), 1, white)
                screen.blit(text, (paddleA.rect.x + 10,paddleA.rect.y + 20)) #draw lives
                print("Drew Lives")
                pygame.display.flip()

                #Pause
                pygame.time.delay(3000)

                #Make New Ball
                all_sprites_list.remove(ball)
                ball = Ball(white, 10, 10)
                all_sprites_list.add(ball)

                #Reset All Positions
                ball.rect.x = 350
                ball.rect.y = 520
                paddleA.rect.x = 300
                
                
                #Reset the velocity
                all_sprites_list.update()

                #go.
             
                lives -= 1
                if lives <= 0: #If out of lives
                    #update display for lives in the corner
                    lives = 0
                    print("Stop Running")

                    #Game Over
                    font = pygame.font.Font(None, 74) 
                    text = font.render("YOU LOSE", 1, white)
                    screen.blit(text, (250,300))

                    #Points
                    font = pygame.font.Font(None, 34)
                    text = font.render("Points: " + str(score), 1, white)
                    screen.blit(text, (250,400))

                    #Lives Clear
                    text = font.render("Lives 1", 1, black)
                    screen.blit(text, (650, 10)) #draw lives

                    #Lives (same font as before)
                    text = font.render("Lives 0", 1, white)
                    screen.blit(text, (650, 10)) #draw lives

                    #Update screen
                    pygame.display.update()

                    #Pause for effect...
                    pygame.time.wait(3000)

                    #Back To Main Menu
                    running = False 
                
            
                
            #Bounce against the paddles
            if pygame.sprite.collide_mask(ball, paddleA):
                #Sound
                if sound == 1: #if sound is enabled
                    mixer.music.stop()
                    mixer.music.load(C)
                    mixer.music.play()
                #Movement
                ball.rect.y -= 10
                ball.bounce()

            #Bounce against bricks
            brick_current_collides = pygame.sprite.spritecollide(ball,all_bricks,False)
            for brick in brick_current_collides:

                #Sound
                if sound == 1: #if sound is enabled
                    mixer.music.stop()
                    mixer.music.load(E)
                    mixer.music.play()

                #Score
                score += 1
                
                #Mecahnics
                brick.kill()
                ball.bounce()

                #Win Conditions
                if len(all_bricks)==0: #If there are no bricks left, you win
                    font = pygame.font.Font(None, 65)
                    text = font.render("YOU WIN", 1, white)
                    screen.blit(text, (200,300))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = 0  #stop the game
                
#DRAWING


        
        #Drawing
        screen.fill(black) #Background
        all_sprites_list.draw(screen) #Sprites

        #Drawing Text
        font = pygame.font.Font(None, 34)
        text = font.render("Points: " + str(score), 1, white)
        screen.blit(text, (20,10)) #draw points
        text = font.render("Lives " + str(lives), 1, white)
        screen.blit(text, (650, 10)) #draw lives

#!      #Drawing Lives Under Paddle Before Firing
        if real_deployed == False:
            font = pygame.font.Font(None, 34)
            text = font.render("Lives " + str(lives), 1, white)
            screen.blit(text, (paddleA.rect.x + 10,paddleA.rect.y + 10)) #draw lives
        
#UPDATES
        
        #always update everything
#!      
        all_sprites_list.update()
        fake_ball.update()
        fake_ball.checkbounds()
        paddleA.update()
        paddleA.checkbounds()
        pygame.display.flip() #update display
        clock.tick(60) #this code gives us our 60FPS.

    
