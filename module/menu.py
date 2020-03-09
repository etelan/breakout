#Menu System
def main():

    #Import
    import pygame
    import classic #This is our classic game
    from cursor import Cursor
    
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
        text = font.render("MAIN MENU", 1, white) # LINE ONE
        screen.blit(text, (250,50))

        
        #Lines Draw
        font = pygame.font.Font(None, 35)
        text = font.render("Classic Game", 1, white) # LINE ONE
        screen.blit(text, (250,175))

        text = font.render("Game With Extras", 1, white) # LINE ONE
        screen.blit(text, (250,215))

        text = font.render("Settings", 1, white) # LINE ONE
        screen.blit(text, (250,255))
        
        pygame.display.flip()#update
        clock.tick(60)

        #Main Event Loop
        for event in pygame.event.get():
            #Quit Event
            if event.type == pygame.QUIT: #press quit button
                pygame.quit()

            #Key Down Event
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_s: 
                    if cursor.rect.y != 262: #Go Down
                        cursor.rect.y += 40
                if event.key ==pygame.K_w: #Go Up
                    if cursor.rect.y != 182:
                        cursor.rect.y -= 40
                    
                if event.key ==pygame.K_SPACE:
                    if cursor.rect.y == 262:
                        print("Not Done Yet")
                    elif cursor.rect.y == 222:
                        print("Not Done Yet")
                    elif cursor.rect.y == 182:
                        classic.main() #Move it on to classic


                        
                

    

