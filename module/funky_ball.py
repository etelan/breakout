#Imports
import pygame
from random import randint

#Variable for making the ball real.
ball_swapped = false

#Colours
BLACK = (0,0,0)

class Fake_Ball(pygame.sprite.Sprite): #new classed based on sprite class

    #Create
    def __init__(self, colour, width, height):

        super().__init__() #grab the parent contructor

        #Pass in our values
        self.image = pygame.Surface((width,height)) #makes rectangle, for ball haha
        self.image.fill(BLACK) #Background colour is black
        self.image.set_colorkey(BLACK) #also, transparent background

        #Draw the ball
        pygame.draw.rect(self.image, colour, [0, 0, width, height]) #draws our rectangle ball

        #Grab dimensions of ball
        self.rect = self.image.get_rect()

        #It's a funky ball!
        #So no velocity, no fancy stuff, until we press space.
        self.velocity = [0,0]
        
        #Mirror the paddle initially.
        #Which we will do on the main script.

        
        #It will move normally.
        def update(self): #move the ball based on velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        def bounce(self):
        self.velocity[0] = self.velocity[0] #horizontal bounces equally
        self.velocity[1] = -self.velocity[1] #vertical bounces equally


        running = True

        #Main Loop                      
        while(running):
            

            #Main User Event Loop
            for event in pygame.event.get():

                
                #Detect space bar for the velocity give.
                #Key Down Event
                elif event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_SPACE: #press L to also quit
                        running = False

        

        
        

        
        
        
        
