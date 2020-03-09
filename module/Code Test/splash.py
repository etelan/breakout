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
    pygame.display.set_caption("Breakout")

    running = 1


    while(running):

        #Background
        screen.fill(black)
            
        #Write my Splash
        font = pygame.font.Font(None, 74)
        text = font.render("ETELAN", 1, white) # game over
        screen.blit(text, (250,300))

        font = pygame.font.Font(None, 74)
        text = font.render("GAMES", 1, white) # game over
        screen.blit(text, (250,350))

        
        pygame.display.flip()#update
        clock.tick(60)

        #Main Event Loop
        for event in pygame.event.get():
            #Quit Event
            if event.type == pygame.QUIT: #press quit button
                pygame.quit()

        pygame.time.wait(2000)
        running = 0
        #move on from splash screen



    

