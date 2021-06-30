import pygame #importing pygame python module 

# Importing random module for food 
import random 

import colors_Initialising as colorsinit # importing a module storing color 
# pygame initialisation 
pygame.init()

# Initialising hight and width 
display_height = 650
display_width = 400

# Creating a display 
GameWindow = pygame.display.set_mode((display_height, display_width)) #setting resolution 
pygame.display.set_caption("Snake Game ")     # Game Title 
d_update = pygame.display.update() # used to update/ make changes in  a program

# Creating Game specific variables
exit_game = False
game_over = False
snake_x  = 10 
snake_y  = 10
snake_sizeb = 15
snake_length = 15
velocity_x = 0
velocity_y = 0
apple_y = random.randint(0,display_height/2)
apple_x = random.randint(0,display_width/2)
apple_height = 15 
apple_width  = 15
#Score 
score = 0
# Creating a Clock for game  
clock = pygame.time.Clock()

# Defining the fps of game 
fps = 20
#___________________________________________________________________________

#creating a game loop 
while not exit_game:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:   # using if/else for quiting program  
            exit_game = True            # Changing Exit_game value to True restulting in breaking of loop 
        
        # this line of code will allow the snake object to move in velocity 
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = 7
                    velocity_y = 0
                    
        # This line of code will allow the snake object to move in left direction 

                if event.key == pygame.K_LEFT:
                    velocity_x = -7
                    velocity_y =  0          

        # This will help snake move in velocity y move up 
                if event.key == pygame.K_UP:
                    velocity_y = - 7
                    velocity_x = 0
        
        # This will move snake down 
                if event.key == pygame.K_DOWN:
                    velocity_y = 7
                    velocity_x =0  

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    if abs(snake_x -apple_x)<10 and abs(snake_y - apple_y)<10:
        score += 1
        print("score :",score)
        apple_y = random.randint(0,display_height/2)
        apple_x = random.randint(0,display_width/2)

    GameWindow.fill(colorsinit.light_blue)
    pygame.draw.rect(GameWindow, colorsinit.red, [apple_y , apple_x ,apple_height , apple_width], width=0)
    pygame.draw.rect(GameWindow, colorsinit.black,[snake_x , snake_y , snake_length,snake_sizeb], width=0)
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()
quit()

