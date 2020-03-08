#Imports
import pygame

#Colours
black = (0,0,0)

class Brick(pygame.sprite.Sprite): #class based on sprite class

    def __init__(self,colour,width,height):
        #use the sprite constructor
        super().__init__()

        #Make the brick
        self.image = pygame.Surface((width, height))
        self.image.fill(black)
        self.image.set_colourkey(Black)

        #Draw the brick
        pygame.draw.rect(self.image, colour, [0,0,width,height])

        #Grab Co-ords
        self.rect = self.image.get_rect()
        
