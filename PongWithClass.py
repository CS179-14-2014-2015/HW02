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
        self.rect.y = 0
        
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, diameter):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.Surface([diameter, diameter])
    	self.image.fill(BLACK)
    	pygame.draw.circle(self.image, color, (diameter/2, diameter/2), diameter/2)
    	self.rect = self.image.get_rect()
    	self.rect.x = SCREEN_WIDTH/2
    	self.rect.y = SCREEN_HEIGHT/2
       	
    def move(self, x_dir, y_dir, walls, paddles):
        
        self.rect.x += x_dir*BALL_SPEED
        self.rect.y += y_dir*BALL_SPEED   
        walls_hit = pygame.sprite.spritecollide(self, walls, False)
        for wall in walls_hit:
            if y_dir == DOWN:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom
        paddles_hit = pygame.sprite.spritecollide(self, paddles, False)                
        for paddle in paddles_hit:
            if x_dir == RIGHT:
                self.rect.right = paddle.rect.left
            else:
                self.rect.left = paddle.rect.right

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
clock = pygame.time.Clock()

while not endGame:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endGame = True
        #if event.type == KEYDOWN:
        #    if event.key == K_SPACE:
        #        ball.move(RIGHT, walls_list, paddles_list) 
                                    
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        rightPaddle.update(UP, walls_list)
    elif keys[pygame.K_DOWN]:
        rightPaddle.update(DOWN, walls_list)
    elif keys[pygame.K_w]:
        leftPaddle.update(UP, walls_list)
    elif keys[pygame.K_s]:
        leftPaddle.update(DOWN, walls_list) 
    elif keys[pygame.K_SPACE]:
        ball.move(RIGHT, 0, walls_list, paddles_list)
    else:
        print "Unidentified Key"
         
    #-- Set screen color --
    screen.fill(BLACK)

    #-- Display all sprites --
    all_sprites_list.draw(screen)

    #-- Update the screen --
    pygame.display.flip()
    clock.tick(100)
        
pygame.quit()
sys.exit()