#Settings Screen
def main():

    #Import
    import pygame
    from cursor_settings import Cursor
    from pygame import mixer #for sound

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
        f.write("[Paddle Speed]\n4" )
        f.write("\n[Sound]\0" )
        paddle_speed = int(4)
        sound = 0
        #Close the file
        f.close()
    
    #Initialize
    pygame.init() 
    clock = pygame.time.Clock()
    
    #Colours
    black = [0,0,0]
    white = [255,255,255]

    #Dimensions
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Breakout - Settings")

    #Make Cursor
    cursor = Cursor(white, 10,10)
    cursor.rect.x = 200
    cursor.rect.y = 182

    #List
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(cursor)  

    #Running Variable
    running = 1


    while(running):

        #Background Draw
        screen.fill(black)

        #Sprites Draw
        all_sprites_list.draw(screen)

        #Title Draw
        font = pygame.font.Font(None, 74)
        text = font.render("MAIN MENU", 1, white) 
        screen.blit(text, (250,50))


        #Explain1 Draw
        font = pygame.font.Font(None, 25)
        text = font.render("Press 'Space' on 'Save' to save.", 1, white) 
        screen.blit(text, (250,295))

        #Explain2 Draw
        font = pygame.font.Font(None, 25)
        text = font.render("To change a value, use keys 'A' and 'D'.", 1, white) 
        screen.blit(text, (250,335))

        #Explain3 Draw
        font = pygame.font.Font(None, 25)
        text = font.render("This screen will always make a confirmation sound.", 1, white) 
        screen.blit(text, (250,375))
        
        #Paddle Speed Draw
        font = pygame.font.Font(None, 35)
        text = font.render("Paddle Speed: " + str(paddle_speed), 1, white) 
        screen.blit(text, (230,175))

        #Sound Draw Variable Set 
        if sound == 1:
            sound_draw = "On"
        if sound == 0:
            sound_draw = "Off"
        

        #Sound Variable Draw
        text = font.render("Sound: " + str(sound_draw), 1, white) 
        screen.blit(text, (230,215))

        #Save Draw
        text = font.render("Save", 1, white) 
        screen.blit(text, (230,255))
        
        pygame.display.flip()#update
        clock.tick(60)

        #Main Event Loop
        for event in pygame.event.get():
            #Quit Event
            if event.type == pygame.QUIT: #press quit button
                pygame.quit()

            #Key Down Event
            elif event.type == pygame.KEYDOWN:
                
                #Go Down
                if event.key ==pygame.K_s: 
                    if cursor.rect.y != 262: 
                        cursor.rect.y += 40
                #Go Up
                if event.key ==pygame.K_w: 
                    if cursor.rect.y != 182:
                        cursor.rect.y -= 40

                #Close Settings
                if event.key ==pygame.K_BACKSPACE: 
                    running = False

                #Save the Settings    
                if event.key ==pygame.K_SPACE:
                    if cursor.rect.y == 262: #Save                  
                        #File Handing
                        f = open("settings.txt", "w") #open
                        #Save Values
                        f.write("[Paddle Speed]\n")
                        f.write(str(paddle_speed))
                        f.write("\n[Sound]\n")
                        f.write(str(sound))
                        #Close the file
                        f.close()

                        #Success Sound
                        mixer.init()
                        mixer.music.load("Etrim.wav")
                        mixer.music.play()

                        

                #A
                if event.key ==pygame.K_a:
                    if cursor.rect.y == 222: #Sound
                        sound = 0
                    elif cursor.rect.y == 182: #Speed
                        if paddle_speed != 1: #Make sure it is not negative
                            paddle_speed -= 1
                #D
                if event.key ==pygame.K_d:
                    if cursor.rect.y == 222: #Sound
                        sound = 1
                    elif cursor.rect.y == 182: #Speed
                        if paddle_speed != 10: #Make sure it is not too high
                            paddle_speed += 1
      
               
                        


                        
                

    

