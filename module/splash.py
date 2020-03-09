#Splash screen
def main():
    import pygame # import
    pygame.init() #initialize
    clock = pygame.time.Clock() #init clock

    #Colours
    black = [0,0,0]
    white = [255,255,255]

    #Dimensions
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))

    #Caption
    pygame.display.set_caption("Breakout - Splash") 

    running = 1 #How to break the loop


    while(running):

        #Background
        screen.fill(black)
            
        #Write my Splash
        font = pygame.font.Font(None, 74)
        text = font.render("ETELAN", 1, white) # LINE ONE
        screen.blit(text, (250,300))

        font = pygame.font.Font(None, 74)
        text = font.render("GAMES", 1, white) # LINE TWO
        screen.blit(text, (250,350))

        font = pygame.font.Font(None, 20)
        text = font.render("[PRESS SPACE TO CONTINUE]", 1, white) # LINE Three
        screen.blit(text, (250,400))

        
        pygame.display.flip()#update
        clock.tick(60)

        #Main Event Loop
        for event in pygame.event.get():
            #Quit Event
            if event.type == pygame.QUIT: #press quit button
                pygame.quit()

            #Key Down Event
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE: #press L to also quit
                    running = False
                    #move on from splash screen

print("Splashing switftly on...")
    

