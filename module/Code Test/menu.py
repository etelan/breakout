#Menu System
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
    pygame.display.set_caption("Breakout - Menu")

    running = 1


    while(running):

        #Background
        screen.fill(black)
            
        #Write my title
        font = pygame.font.Font(None, 74)
        text = font.render("MAIN MENU", 1, white) # LINE ONE
        screen.blit(text, (250,50))

        
        #Write my lines
        font = pygame.font.Font(None, 35)
        text = font.render("Classic Game", 1, white) # LINE ONE
        screen.blit(text, (250,175))
        
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
main()



    

