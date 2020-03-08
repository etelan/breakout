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
        self.image = pygame.Surface((width,height))  #Creates box image
        self.image.fill(BLACK) #Fills background box
        self.image.set_colorkey(BLACK) #Transparent Background


        #drawing the paddle
        pygame.draw.rect(self.image, colour, [0,0, width, height]) 

        #Get the coords
        self.rect = self.image.get_rect() 

        #Speed
        self.movement = [0,0] #movement format shall be x,y
        self.speed = 4 #speed of paddle

    def update(self):
        self.rect = self.rect.move(self.movement) #sets coords to the movement.

    def checkbounds(self): #are we out of boudns?
        if self.rect.left < 0: #if we are too far left, we're out of bounds.
            self.rect.x = 0 #set to 0 if below 0
        if self.rect.right > 600: # if too far right, we're out of bounds.
            self.rect.x = 600 - 100
        
        




    
