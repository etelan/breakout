#fix ball when paddle moves

#Imports
import pygame
from random import randint

#Colours
BLACK = (0,0,0)

class Cursor(pygame.sprite.Sprite): #new classed based on sprite class

    #Create
    def __init__(self, colour, width, height):

        super().__init__() #grab the parent contructor

        #Pass in our values
        self.image = pygame.Surface((width,height)) #makes rectangle
        self.image.fill(BLACK) #Background colour is black
        self.image.set_colorkey(BLACK) #also, transparent background

        #Draw the Cursor
        pygame.draw.rect(self.image, colour, [0, 0, width, height]) #draws our rectangle ball

        #Grab dimensions of ball
        self.rect = self.image.get_rect()

        
        

        
        

        
        
        
        
