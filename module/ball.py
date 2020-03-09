#Imports
import pygame
from random import randint

#Colours
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite): #new classed based on sprite class

    #Create
    def __init__(self, colour, width, height):

        super().__init__() #grab the parent contructor

        #Pass in our values
        self.image = pygame.Surface((width,height)) #makes rectangle, for ball haha
        self.image.fill(BLACK) #Background colour is black
        self.image.set_colorkey(BLACK) #also, transparent background

        #Draw the ball
        pygame.draw.rect(self.image, colour, [0, 0, width, height]) #draws our rectangle ball

        #Because it has displacement, not just distance, we need velocity[x,y] with a random starting speed
        self.velocity = [randint(-8,8), randint(-8,-3)]

        

        #Grab dimensions of ball
        self.rect = self.image.get_rect()

    def update(self): #move the ball based on velocity
        
        #Make sure it doesn't get stuck.
        if self.velocity[0] == 1 or self.velocity[0] == 0:
            self.velocity[0] = randint(-8,8)
            
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = self.velocity[0] #horizontal bounces equally
        self.velocity[1] = -self.velocity[1] #vertical bounces equally
        

        
        
        
        
