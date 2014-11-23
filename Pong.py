import pygame, sys, random
from pygame.locals import * #for pygame variables

#-- Global Constants --
FEIND = (89,79,79)
LIGHTBLUE = (69,173,168)
WHITE = (229,252,194)
BLUE = (84,121,128)
GREEN = (237,201,81)
RED = (204,51,63)
SCORE_BOARD_COLOR = (157,224,173, 90)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

BALL_DIAMETER = 15
speed_x = 3
speed_y = 3

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
L_PADDLE_XPOS = 10
L_PADDLE_YPOS = SCREEN_HEIGHT/2
R_PADDLE_XPOS = SCREEN_WIDTH - 2*L_PADDLE_XPOS
R_PADDLE_YPOS = SCREEN_HEIGHT/2
PADDLE_DISPLACEMENT = 5

WALL_WIDTH = 5
SCORE_WALL_WIDTH = 1

SCORE_BOARD_WIDTH = 100
SCORE_BOARD_HEIGHT = 50

NET_WIDTH = 2

#Paddles Directions
UP = -1
DOWN = 1

#-- Classes --
class Net(pygame.sprite.Sprite):
    def __init__(self, color, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, SCREEN_HEIGHT-2*WALL_WIDTH])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH/2
        self.rect.y = WALL_WIDTH
        
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, diameter):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.Surface([diameter, diameter])
    	self.image.fill(FEIND)
    	pygame.draw.circle(self.image, color, (diameter/2, diameter/2), diameter/2)
    	self.rect = self.image.get_rect()
    	self.rect.x = random.randint(SCREEN_WIDTH/3, 2*SCREEN_HEIGHT/3)
    	self.rect.y = random.randint(SCREEN_HEIGHT/3, 2*SCREEN_HEIGHT/3) 	
    	self.dx = speed_x #Speed in x direction
    	self.dy = speed_y #Speed in y direction
  	
    def move(self): 
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        
    def checkCollision(self, walls, paddles):
        walls_hit = pygame.sprite.spritecollide(self, walls, False)
        for wall in walls_hit:
            if self.rect.bottom <= SCREEN_HEIGHT + WALL_WIDTH and self.rect.bottom >= SCREEN_HEIGHT - WALL_WIDTH:
                self.dy *= -1
            if self.rect.top <= WALL_WIDTH and self.rect.top >= -1 * WALL_WIDTH:
                self.dy *= -1   
        paddles_hit = pygame.sprite.spritecollide(self, paddles, False)                
        for paddle in paddles_hit:
            if self.rect.right <= SCREEN_WIDTH and self.rect.right >= SCREEN_WIDTH - 2 * PADDLE_WIDTH:
                self.dx *= -1
            if self.rect.left <= 2 * PADDLE_WIDTH and self.rect.left >= -1 * PADDLE_WIDTH:
                self.dx *= -1    
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            if self.rect.right >= SCREEN_WIDTH:
                playerOne.addScore()
            if self.rect.left <= 0:
                playerTwo.addScore()
            self.rect.x = random.randint(SCREEN_WIDTH/3, 2*SCREEN_HEIGHT/3)
            self.rect.y = random.randint(SCREEN_HEIGHT/3, 2*SCREEN_HEIGHT/3) 

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def move(self, y_dir, walls):
        self.rect.y += y_dir*PADDLE_DISPLACEMENT    
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if y_dir == DOWN:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Wall(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Score(pygame.sprite.Sprite):
    def __init__(self, x_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([SCORE_BOARD_WIDTH, SCORE_BOARD_HEIGHT])
        self.image.fill(FEIND)
        self.rect = self.image.get_rect()
        self.rect.centerx = x_pos
        self.rect.centery = SCREEN_HEIGHT/4
        self.score = 0
        self.font = pygame.font.Font("chargen.ttf", 250)
        self.image = self.font.render(("%r" %self.score), False, SCORE_BOARD_COLOR)
        
    def addScore(self):
        self.score += 1
        self.image = self.font.render(("%r" %self.score), False, SCORE_BOARD_COLOR)
        
        
#-- Pygame Initializing --
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Pong")


font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Hello, World", True, (0, 128, 0))
screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

#-- Sprite Objects List --
paddles_list = pygame.sprite.Group()
walls_list = pygame.sprite.Group()
score_walls_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#-- Create a Net --
net = Net(GREEN, NET_WIDTH)
all_sprites_list.add(net)

#-- Create a Score board --
playerOne = Score(SCREEN_WIDTH/4)
playerTwo = Score(3*SCREEN_WIDTH/4)
all_sprites_list.add(playerOne)
all_sprites_list.add(playerTwo)

ball = Ball(WHITE, BALL_DIAMETER)
all_sprites_list.add(ball)


#-- Create Paddles --
leftPaddle = Paddle(LIGHTBLUE, PADDLE_WIDTH, PADDLE_HEIGHT, L_PADDLE_XPOS, L_PADDLE_YPOS)
rightPaddle = Paddle(LIGHTBLUE, PADDLE_WIDTH, PADDLE_HEIGHT, R_PADDLE_XPOS, R_PADDLE_YPOS)
all_sprites_list.add(leftPaddle, rightPaddle)
paddles_list.add(leftPaddle, rightPaddle)

#-- Create a Wall -- 
topWall = Wall(BLUE, 0, SCREEN_HEIGHT - WALL_WIDTH, SCREEN_WIDTH, WALL_WIDTH)
bottomWall = Wall(BLUE, 0, 0, SCREEN_WIDTH, WALL_WIDTH)
walls_list.add(topWall, bottomWall)
all_sprites_list.add(topWall, bottomWall)

#-- Create Red Walls --
leftWall = Wall(RED, L_PADDLE_XPOS, WALL_WIDTH, SCORE_WALL_WIDTH, SCREEN_HEIGHT-2*WALL_WIDTH)
rightWall = Wall(RED, R_PADDLE_XPOS+PADDLE_WIDTH, WALL_WIDTH, SCORE_WALL_WIDTH, SCREEN_HEIGHT-WALL_WIDTH)
all_sprites_list.add(leftWall, rightWall)
score_walls_list.add(leftWall, rightWall)

#-- Variable to end the game --
endGame = False

#-- Pygame Clock --
clock = pygame.time.Clock()

#-- Game loop --
while not endGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endGame = True
    #-- Player Controls [Right Paddle: Arrow Up and Arrow Down Keys] --                                       
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        rightPaddle.move(UP, walls_list)
    if keys[pygame.K_DOWN]:
        rightPaddle.move(DOWN, walls_list)
    #-- Player Controls [Left Paddle: W for up and S for down] --  
    if keys[pygame.K_w]:
        leftPaddle.move(UP, walls_list)
    if keys[pygame.K_s]:
        leftPaddle.move(DOWN, walls_list) 

    #-- Set screen color --
    screen.fill(FEIND)
    
    #-- Ball movement and Collision detection --
    ball.move()
    ball.checkCollision(walls_list, paddles_list)
    
    #-- Display all sprites --
    all_sprites_list.draw(screen)
    

    #-- move the screen --
    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()
sys.exit()