import pygame # Importing game module 

if __name__ == "__main__": # creatng a mainfunction

    pygame.init()#  initialise the pygame 
    #creating the screen             
    
    # Creating a game window          h  , w 
    screen = pygame.display.set_mode((800,400))    # Setting up resolution 
    pygame.display.set_caption("harshit's First game") # game title 

    # Initialising game specific variavel 
    Exit_game = False  # Initialising the value False 
    Game_Over = False

    # Creating a Game loop 
    while not Exit_game:
        # iterating the events of intput 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # using if/else for quiting program  
                Exit_game = True # Changing Exit_game value to True restulting in breaking of loop 

            # Key pressing right arrow 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("You have right key")
    pygame.quit()
    quit()
    


