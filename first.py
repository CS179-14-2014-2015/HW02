import pygame, sys 
from pygame.locals import * #for pygame variables

#window's configurations
WIN_HEIGHT = 400
WIN_WIDTH = 600
#ball's configuration
INIT_BALL_POSITION = (WIN_WIDTH/2,WIN_HEIGHT/2)
RADIUS = 10
#color format: (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)


pygame.init() #initializes pygame 
DISPLAYSURF = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))#window's size
pygame.display.set_caption('Pong') #window name

#table's configuration
NET_WIDTH = 3
DISPLAYSURF.fill(BLACK) 
pygame.draw.line(DISPLAYSURF, WHITE, (WIN_WIDTH/2,0), (WIN_WIDTH/2, WIN_HEIGHT), NET_WIDTH) #Param: surface, color, start_pos, end_pos, width
leftPaddle_position = [10, 0, 10, 60] #x,y,width,height
rightPaddle_position = [WIN_WIDTH-10, 0, -10, 60] #x,y,width,height
leftPaddle = pygame.draw.rect(DISPLAYSURF, WHITE, leftPaddle_position) #Param: surface, color, area
rightPaddle = pygame.draw.rect(DISPLAYSURF, WHITE, rightPaddle_position) #Param: surface, color, area
ball = pygame.draw.circle(DISPLAYSURF, GRAY, INIT_BALL_POSITION, RADIUS) #Param: surface, color, position, radius, width     

while True: # main game loop
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()