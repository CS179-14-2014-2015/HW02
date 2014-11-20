import pygame
from pygame.locals import *

class Paddle(pygame.sprite.Sprite):
	def __init__(self, x, y):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self) 	
		# Specify surface with dimensions (width x height)
		self.image = pygame.Surface((20,100))
		# Load image and set background to alpha
		pygame.draw.rect(self.image,(255,255,255),[0,0,20,100])
		# get rectangle (surface) attributes (x and y) 
		self.rect = self.image.get_rect()
		# Specify initial coordinates
		self.rect.x = x
		self.rect.y = y
		# Specify reset position
		self.xinit = x
		self.yinit = y
	def moveUp(self):
		self.rect.y -= 10
	#def moveDown JAC LIN

	def checkCollision(self, sprite2):
		result = pygame.sprite.collide_rect(self, sprite2)
		if result == True:
			self.resetPosition()

	def resetPosition(self):
		self.rect.x = self.xinit
		self.rect.y = self.yinit

# Ball class with __init__ JAC LIN

# Wall Class
class Wall(pygame.sprite.Sprite):
	def __init__(self,width,height,x,y):
		pygame.sprite.Sprite.__init__(self) 
		# Specify surface with dimensions (width x height)
		self.image = pygame.Surface((width,height))
		# Load image and set background to alpha
		pygame.draw.rect(self.image,(255,255,255),[0,0,width,height])
		self.rect = self.image.get_rect()
		# Specify initial coordinates
		self.rect.x = x
		self.rect.y = y


# initialize pygame
pygame.init()

# set screen dimensions
screen_width=400
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# This is the sprite list. All you need to know is that this list is used for rendering/updating ALL the graphics/images it has :)
spritesList = pygame.sprite.RenderPlain()

#Declare Walls
topWall = Wall(400,2,0,0)
bottomWall = Wall(400,2,0,398)
leftWall = Wall(2,400,0,0)
rightWall = Wall(2,400,398,0)

#Declare player 1 Paddle with starting X,Y coordinates
player1 = Paddle(20,150)
#declare a player 2 JAC LIN :)

# Add player 1 to spritesList
# Every graphical object should be added to spritesList
spritesList.add(player1,topWall,bottomWall,leftWall,rightWall)


while 1:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            pygame.quit() # Exit Flag
        elif event.type == pygame.KEYDOWN:
        	if event.key==pygame.K_w:
						player1.moveUp()

				# Implement Missing Controls for Player 1 and 2 :)
		
		# Black BG
    screen.fill(0)

    # Draws or "Blits" all the graphics in spritesList
    spritesList.draw(screen)

    player1.checkCollision(topWall)
    #FPS
    clock.tick(40)
    
    # update the screen 
    pygame.display.flip()

