import pygame, sys, random
from pygame.locals import * #for pygame variables

#-- Global Constants --
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0, 80)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

BALL_DIAMETER = 15
BALL_SPEED = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
L_PADDLE_XPOS = 10
L_PADDLE_YPOS = SCREEN_HEIGHT/2
R_PADDLE_XPOS = SCREEN_WIDTH - 2*L_PADDLE_XPOS
R_PADDLE_YPOS = SCREEN_HEIGHT/2
PADDLE_DISPLACEMENT = 5

WALL_WIDTH = 5

NET_WIDTH = 2

UP = -1
DOWN = 1
RIGHT = 1
LEFT = -1

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
    	self.image.fill(BLACK)
    	pygame.draw.circle(self.image, color, (diameter/2, diameter/2), diameter/2)
    	self.rect = self.image.get_rect()
    	self.rect.x = SCREEN_WIDTH/2
    	self.rect.y = SCREEN_HEIGHT/2  	
    	self.dx = 5
    	self.dy = 5
       	
    def move(self): 
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        
    def checkCollision(self, walls, paddles):
        walls_hit = pygame.sprite.spritecollide(self, walls, False)
        for wall in walls_hit:
            if self.rect.bottom == SCREEN_HEIGHT:
                self.dy *= -1
            if self.rect.top == 0:
                self.dy *= -1
        paddles_hit = pygame.sprite.spritecollide(self, paddles, False)                
        for paddle in paddles_hit:
            if self.rect.right == SCREEN_WIDTH-PADDLE_WIDTH:
                self.dx *= -1
            if self.rect.left == PADDLE_WIDTH:
                self.dx *= -1

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, y_dir, walls):
        self.rect.y += y_dir*PADDLE_DISPLACEMENT    
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if y_dir == DOWN:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

#-- Pygame Initializing --
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Pong")

#-- Sprite Objects List --
paddles_list = pygame.sprite.Group()
walls_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#-- Create a Net --
net = Net(GREEN, NET_WIDTH)
all_sprites_list.add(net)

#-- Create a Ball --
ball = Ball(WHITE, BALL_DIAMETER)
all_sprites_list.add(ball)

#-- Create Paddles --
leftPaddle = Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT, L_PADDLE_XPOS, L_PADDLE_YPOS)
rightPaddle = Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT, R_PADDLE_XPOS, R_PADDLE_YPOS)
all_sprites_list.add(leftPaddle, rightPaddle)
paddles_list.add(leftPaddle, rightPaddle)

#-- Create a Wall -- 
topWall = Wall(0, SCREEN_HEIGHT - WALL_WIDTH, SCREEN_WIDTH, WALL_WIDTH)
bottomWall = Wall(0, 0, SCREEN_WIDTH, WALL_WIDTH)
walls_list.add(topWall, bottomWall)
all_sprites_list.add(topWall, bottomWall)

#-- Variable to end the game --
endGame = False

#-- Pygame Clock --
clock = pygame.time.Clock()

#-- Game loop --
while not endGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endGame = True
        #if event.type == KEYDOWN:
        #    if event.key == K_SPACE:
        #        ball.move(LEFT, 0, walls_list, paddles_list)
                                    
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        rightPaddle.update(UP, walls_list)
    elif keys[pygame.K_DOWN]:
        rightPaddle.update(DOWN, walls_list)
    elif keys[pygame.K_w]:
        leftPaddle.update(UP, walls_list)
    elif keys[pygame.K_s]:
        leftPaddle.update(DOWN, walls_list) 
    #elif keys[pygame.K_SPACE]:
    #    ball.move(LEFT, 0, walls_list, paddles_list)
    else:
        print "Unidentified Key"

    #-- Set screen color --
    screen.fill(BLACK)
    
    ball.move()
    ball.checkCollision(walls_list, paddles_list)
    #-- Display all sprites --
    all_sprites_list.draw(screen)

    #-- Update the screen --
    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()
sys.exit()