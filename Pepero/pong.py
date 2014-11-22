import pygame
from pygame.locals import *
from random import choice
import sys

"""
	A Pong Clone by Pepero
Hadrian Lim and Jac Lin Yu
		CS179.14 2014-2015
"""


""" Game Classes """

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
		self.rect.y -= 10

	def moveDown(self):
		self.rect.y += 10

	def checkCollisionPaddle(self, sprite2):
	 	result = pygame.sprite.collide_rect(self, sprite2)
	 	if result == True:
	 		if sprite2 == topWall:
	 			self.rect.y = 0
	 		elif sprite2 == bottomWall:
	 			self.rect.y = 320

class Ball(pygame.sprite.Sprite):
	def __init__(self, x, y, speed = 2):
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
		#random starting directions -1 for left, down; 1 for right, up
		self.horizontal = choice([1, -1])
		self.vertical = choice([1, -1])
		#starting speed
		self.speed = speed

	# returns ints for scoreboard identification
	def checkCollisionBall(self, sprite2, Speedy = True):
		addSpeed = 0
		if Speedy is True:
			addSpeed = 1
	 	result = pygame.sprite.collide_rect(self, sprite2)
	 	if result == True:
	 		if type(sprite2) == Paddle:
	 			self.horizontal *= -1
	 			self.speed += addSpeed
	 			return 0
	 		elif ((sprite2 == topWall) or (sprite2 == bottomWall)):
	 			self.vertical *= -1
	 			return 0
	 		elif sprite2 == leftWall:
	 			self.resetPosition()
	 			return 1
			elif sprite2  == rightWall:
				self.resetPosition()
				return -1
			return 0

	def resetPosition(self):
		self.rect.x = self.xinit
		self.rect.y = self.yinit
		self.horizontal = choice([1, -1])
		self.vertical = choice([1, -1])
			
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

	def stop(self):
		self.speed = 0


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


class Scoreboard(pygame.sprite.Sprite):
	def __init__(self, x, y, score = 0):
		self.score = score
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.Font('scoreboard.ttf', 50)
		self.image = self.font.render(("%r" %self.score), False, (0, 128, 128))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def add(self):
		self.score += 1
		self.image = self.font.render(("%r" %self.score), False, (0, 128, 128))


class DashedLine(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((2, 400))
		pygame.draw.line(self.image, (255, 255, 255), (0,25), (0,40), 2)
		pygame.draw.line(self.image, (255, 255, 255), (0,65), (0,80), 2)
		pygame.draw.line(self.image, (255, 255, 255), (0,105), (0,120), 2)
		pygame.draw.line(self.image, (255, 255, 255), (0,145), (0,160), 2)
		pygame.draw.line(self.image, (255, 255, 255), (0,185), (0,200), 2)
		pygame.draw.line(self.image, (255, 255, 255), (0,225), (0,240), 2)
		pygame.draw.line(self.image, (255, 255, 255), (0,265), (0,280), 2)
		pygame.draw.line(self.image, (255, 255, 255), (0,305), (0,320), 2)
		pygame.draw.line(self.image, (255, 255, 255), (0,345), (0,360), 2)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

""" Game Runtime """


if __name__ == "__main__":

	# Start Menu
	print "2-Player Speed Pong by Hadrian Lim and Jac Lin Yu\n\n"
	print "Player 1 - Use Keys W & A"
	print "Player 2 - Use Arrow Keys Up & Down\n"
	rounds = input("How many rounds do you want to play? (Best out of..): ")
	Speed = raw_input("Do you want progressive ball speed per round? [Y/N]: ")
	anyKey = raw_input('Press enter to play. Have Fun!')	

	if Speed.upper() == 'Y':
		Speedy = True
	else:
		Speedy = False

	if rounds % 2 == 0:
		rounds += 1
	
	# initialize pygame
	pygame.init()

	# set screen dimensions and title
	screen_width, screen_height = 600, 400
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Speed Pong")
	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	# This is the sprite container class. All you need to know is that this class is used for rendering/updating ALL the graphics/images it has :)
	spritesContainer = pygame.sprite.RenderPlain()

	#Declare Walls
	topWall = Wall(500, 2, 50, 0)
	bottomWall = Wall(500, 2, 50, 398)
	leftWall = Wall(2, 500, 50, 0)
	rightWall = Wall(2, 500, 548, 0)

	# Declare Walls list to contain all walls
	Walls = [topWall, bottomWall, leftWall, rightWall]

	#Declare player 1 and 2 Paddles with starting X,Y coordinates
	player1, player2 = Paddle(52, 163), Paddle(546, 163)
	 
	#Declare ball
	ball1 = Ball(295, 195)

	#Declare Scoreboards with starting coordinates
	player1Score, player2Score = Scoreboard(13, 180), Scoreboard(562, 180)
	

	#Declare Middle Line
	middleLine = DashedLine(300, 0)

	# Declare collide list to contain all collide-able elements
	collideList = [player1, player2, ball1] + Walls

	# Add player 1 to spritesContainer
	# Every graphical object should be added to spritesContainer
	spritesContainer.add(player1, player2, ball1, player1Score, player2Score, topWall, bottomWall, leftWall, rightWall, middleLine)


	# Run game loop
	while 1:
		
		# Input Detection
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
				pygame.quit()
				sys.exit() #Exit Flag

		#Black BG
		screen.fill(0)
		
		#Draws all the graphics in spritesContainer
		spritesContainer.draw(screen)

		for x in range(0,2):
			player1.checkCollisionPaddle(Walls[x])
			player2.checkCollisionPaddle(Walls[x])
		
		for graphics in collideList:
			hasScored = ball1.checkCollisionBall(graphics, Speedy)
			if hasScored == 1:
				player2Score.add()
			elif hasScored == -1:
				player1Score.add()
			


		ball1.move()

		if player1Score.score == rounds/2 + 1 or player2Score.score == rounds/2 + 1:
			if player1Score.score > player2Score.score:
				declareWinner = Scoreboard(100,150, 'PLAYER 1 WINS')
			else:
				declareWinner = Scoreboard(100,150, 'PLAYER 2 WINS')	
			spritesContainer.add(declareWinner)
			spritesContainer.remove(ball1, middleLine)
			ball1.stop()
		
		#FPS
		clock.tick(45)

		#update  or "Blits" the screen
		pygame.display.flip()


