#TODO: Add blocks to hit with ball.

#Pygame library for games.
import pygame

#Set the pygame window
pygame.init()
width = 600
height = 400

#Set the display as variable screen.
screen = pygame.display.set_mode((width, height))

#Set Caption
pygame.display.set_caption("Breakout")

#Set Background Colours
red = [255,0,0]
white = [255,255,255]
black = [0,0,0]
green = [0,255,0]


#Set our FPS and clock
FPS = 50
clock = pygame.time.Clock()

#Tell the game to run
running = True

#Paddle Class (a class is a template for an object)
class Paddle():
    
    #Create.
    #This is our contructor. Allows us to set default values.
    def __init__(self,x,y,sizex,sizey,color):

        #Now we create our paddle.
        self.image = pygame.Surface((sizex,sizey), pygame.SRCALPHA, 32) #Blank rectangle. Per-Pixel Alpha. 32 Depth.
        self.rect = self.image.get_rect() #gets the rectangular coordinates
        self.rect.left = x #set x
        self.rect.top = y #set y

        self.image.fill(white) #fill with white

        self.movement = [0,0] #this sets the format for us. [x,y]
        self.speed = 8 #The speed of the paddle. pixels/frame

    #Draw
    def draw(self): 
        screen.blit(self.image, self.rect) #draws paddle on screen.

    #Step
    def update(self):
        self.rect = self.rect.move(self.movement) #sets coords to the movement.

    #Outside Room
    def checkbounds(self): #are we out of boudns?
        if self.rect.left < 0: #if we are too far left, we're out of bounds.
            print("Out of bounds")
            print(self.rect)
            self.rect.left = 0 #set to 0 if below 0
        if self.rect.right > width: # if too far right, we're out of bounds.
            print("Out of bounds")
            print(self.rect)
            self.rect.left = width
        



#Main Loop
myPaddle = Paddle(width/2, height - height/10, 80, 10, white)

            
while(running):
    
    #User events at each frame
    for event in pygame.event.get():
        
        #Quit.
        if event.type == pygame.QUIT:
            #Set running to false, as we want it to quit.
            running = False
            pygame.quit() #close the window
            quit() #quit the program
    
        #Keys Released Code
        if event.type == pygame.KEYUP:
            # if (left) or (right) are released
            if event.key == (pygame.K_LEFT or ord('a')) or event.key == (pygame.K_RIGHT or ord('d')):
                myPaddle.movement[0] = 0

    #Keys Held
    pressedKeys = pygame.key.get_pressed()
    
    #Keys Held Code
    #Left
    if pressedKeys[pygame.K_LEFT] or pressedKeys[ord('a')]:
        print("left detected")
        myPaddle.movement[0] = -1*myPaddle.speed
    #Right
    if pressedKeys[pygame.K_RIGHT] or pressedKeys[ord('d')]:
        print("right detected")
        myPaddle.movement[0] = myPaddle.speed

    

    

    #always update everything
    screen.fill(green) #colour
    myPaddle.update() #update paddle
    myPaddle.checkbounds() #out of bounds check
    myPaddle.draw() #draw paddle
    pygame.display.update() #update display

    #Background update
    clock.tick(FPS) #this code gives us our 50FPS.
    
