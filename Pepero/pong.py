import pygame
from pygame.locals import *
from random import choice

class Scoreboard(pygame.sprite.Sprite):
	def __init__(self, x, y):
		self.score = 0
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.Font('scoreboard.ttf', 50)
		self.image = self.font.render(("%r" %self.score), False, (0, 128, 128))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def add(self):
		self.score += 1

	def getscore(self):
		score

class Paddle(pygame.sprite.Sprite):
	def __init__(self, x, y):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self) 	
		# Specify surface with dimensions (width x height)
		self.image = pygame.Surface((5, 75))
		# Load image and set background to alpha
		pygame.draw.rect(self.image, (255, 255, 255), [0, 0, 5, 75])
		# get rectangle (surface) attributes (x and y) 
		self.rect = self.image.get_rect()
		# Specify initial coordinates
		self.rect.x = x
		self.rect.y = y

	def moveUp(self):
		self.rect.y -= 5

	def moveDown(self):
		self.rect.y += 5

	def checkCollisionPaddle(self, sprite2):
	 	result = pygame.sprite.collide_rect(self, sprite2)
	 	if result == True:
	 		if sprite2 == topWall:
	 			self.rect.y = 320
	 		elif sprite2 == bottomWall:
	 			self.rect.y = 0

# Ball class
class Ball(pygame.sprite.Sprite):
	def __init__(self, x, y, speed = 3):
    #inherit constructor from Sprite class
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10, 10))
		pygame.draw.circle(self.image, (255, 255, 255), (5, 5), 5)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		# Specify reset position
		self.xinit = x
		self.yinit = y
		#random starting directions
		self.horizontal = choice([1, -1])
		self.vertical = choice([1, -1])
		#starting speed
		self.speed = speed

	def checkCollisionBall(self, sprite2):
	 	result = pygame.sprite.collide_rect(self, sprite2)
	 	if result == True:
	 		if type(sprite2) == Paddle:
	 			self.horizontal *= -1
	 		elif ((sprite2 == topWall) or (sprite2 == bottomWall)):
	 			self.vertical *= -1
	 		elif sprite2 == leftWall:
	 			self.resetPosition()
			elif sprite2  == rightWall:
				self.resetPosition()

	def resetPosition(self):
		self.rect.x = self.xinit
		self.rect.y = self.yinit
		self.horizontal = choice([1, -1])
		self.vertical = choice([1, -1])

	def changeDirection(self):
		if self.checkCollision.result == True:
		 	if type(sprite2) == Paddle :
		 		horizontal *= -1
		 	elif type(sprite2) == Wall:
		 		vertical *= -1
			
	def move(self):
		if self.horizontal == 1:
			if self.vertical == 1:
				self.rect.x += self.speed
				self.rect.y -= self.speed
			elif self.vertical == -1:
				self.rect.x += self.speed
				self.rect.y += self.speed
		elif self.horizontal == -1:
			if self.vertical == 1:
				self.rect.x -= self.speed
				self.rect.y -= self.speed
			elif self.vertical == -1:
				self.rect.x -= self.speed
				self.rect.y += self.speed

# Wall Class
class Wall(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		pygame.sprite.Sprite.__init__(self) 
		# Specify surface with dimensions (width x height)
		self.image = pygame.Surface((width, height))
		# Load image and set background to alpha
		pygame.draw.rect(self.image, (0, 0, 0), [0, 0, width, height])
		self.rect = self.image.get_rect()
		# Specify initial coordinates
		self.rect.x = x
		self.rect.y = y


# initialize pygame
pygame.init()

# set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# This is the sprite list. All you need to know is that this list is used for rendering/updating ALL the graphics/images it has :)
spritesList = pygame.sprite.RenderPlain()

#Declare Walls
topWall = Wall(500, 2, 50, 0)
bottomWall = Wall(500, 2, 50, 398)
leftWall = Wall(2, 500, 50, 0)
rightWall = Wall(2, 500, 548, 0)

#Declare player 1 Paddle with starting X,Y coordinates
player1 = Paddle(48, 163)

#Declare player 2 Paddle with starting X,Y coordinates
player2 = Paddle(546, 163)

#Declare ball
ball1 = Ball(295, 195)

player1Score = Scoreboard(13, 180)
player2Score = Scoreboard(562, 180)

# Add player 1 to spritesList
# Every graphical object should be added to spritesList
spritesList.add(player1, player2, ball1, player1Score, player2Score, topWall, bottomWall, leftWall, rightWall)

while 1:
	ball1.move()
	#newBall.rect.move_ip(horizontal,vertical)
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_w]:
		player1.moveUp()
	if pressed[pygame.K_s]:
		player1.moveDown()
	if pressed[pygame.K_UP]:
		player2.moveUp()
	if pressed[pygame.K_DOWN]:
		player2.moveDown()

	for event in pygame.event.get(): #User did something
		if event.type == pygame.QUIT: #If user clicked close
			pygame.quit() #Exit Flag

	#Black BG
	screen.fill(0)
	
	#Draws or "Blits" all the graphics in spritesList
	spritesList.draw(screen)

	player1.checkCollisionPaddle(topWall)
	player1.checkCollisionPaddle(bottomWall)
	player2.checkCollisionPaddle(topWall)
	player2.checkCollisionPaddle(bottomWall)
	
	ball1.checkCollisionBall(player1)
	ball1.checkCollisionBall(player2)
	ball1.checkCollisionBall(topWall)
	ball1.checkCollisionBall(bottomWall)
	ball1.checkCollisionBall(leftWall)
	ball1.checkCollisionBall(rightWall)

	#FPS
	clock.tick(40)

	#update the screen
	pygame.display.flip()


