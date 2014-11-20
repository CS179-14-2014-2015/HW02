import pygame
from pygame.locals import *

class Paddle(pygame.sprite.Sprite):
	def __init__(self, x, y):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self) 	
		# Specify surface with dimensions (width x height)
		self.image = pygame.Surface((20,100))
		# Load image and set background to alpha
		self.image = pygame.image.load('paddle.png').convert_alpha()
		# get rectangle (surface) attributes (x and y) 
		self.rect = self.image.get_rect()
		# Specify initial coordinates
		self.rect.x = x
		self.rect.y = y
	def moveUp(self):
		self.rect.y -= 10
	#def moveDown JAC LIN

# Ball class with __init__ JAC LIN

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

#Declare player 1 Paddle with starting X,Y coordinates
player1 = Paddle(50,200)
#declare a player 2 JAC LIN :)

# Add player 1 to spritesList
# Every graphical object should be added to spritesList
spritesList.add(player1)

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

    #FPS
    clock.tick(40)
    
    # update the screen 
    pygame.display.flip()

