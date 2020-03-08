import pygame
BLACK = (0,0,0)

#Paddle Class (a class is a template for an object)
class Paddle(pygame.sprite.Sprite): #Tells python this is a sprite class.
    
    #Create
    #This is our contructor. Allows us to set default values.
    def __init__(self, colour, width, height):

        #Sprite Constructor (parent contructor)
        super().__init__()


        #Now we create our paddle.
        self.image = pygame.Surface((width,height)) 
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)


        #drawing the paddle
        pygame.draw.rect(self.image, colour, [0,0, width, height])

        #Get the coords
        self.rect = self.image.get_rect()



    
