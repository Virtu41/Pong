# imports pygame
import pygame
import time
# initializes pygame
pygame.init()

# declares clock
clock = pygame.time.Clock()	

# defines some colours
gray = (80, 80, 80)
light_gray = (200, 200, 200)
white = (255, 255, 255)
darkblue = (33, 36, 46)
black = (0, 0, 0)

# defines game display
display_width = 700
display_height = 500
gameDisplay = pygame.display.set_mode((display_width, display_height))

# sets the caption and icon
pygame.display.set_caption("Atari Pong")
icon = pygame.image.load("Atari-Logo.png")
pygame.display.set_icon(icon)

audio1= pygame.mixer.music.load("Pouya - Sharab OFFICIAL TRACK.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# loads background images
wasdinstructions = pygame.image.load("WASDandArrowkeys.png")
wasdinstructions = pygame.transform.scale(wasdinstructions,(300,151))
background = pygame.image.load("pong.jpg")
background = pygame.transform.scale(background,(700, 300))
background_level1 = pygame.image.load("black.png")
background_level1 = pygame.transform.scale(background_level1, (700, 500))
instructions = pygame.image.load("black.png")
instructions = pygame.transform.scale(instructions, (700, 500))


#declares some variables 
unlocked = False
score = 10000
openchest = False

#allows text to be displayed
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

# defines message display
def message_display(text):
    #declares the font and font size 
    smallText = pygame.font.Font("freesansbold.ttf", 50)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((display_width/2),(display_height/4))
    gameDisplay.blit(TextSurf, TextRect)
    
def message_display1(text):
    #declares the font and font size 
    smallText = pygame.font.Font("freesansbold.ttf", 15)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((215),(200))
    gameDisplay.blit(TextSurf, TextRect)
    
def message_display2(text):
    #declares the font and font size 
    smallText = pygame.font.Font("freesansbold.ttf", 15)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((265),(250))
    gameDisplay.blit(TextSurf, TextRect)
    
def message_display3(text):
    #declares the font and font size 
    background = gameDisplay.fill(black)
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(3)
    
def message_display4(text):
    #declares the font and font size 
    smallText = pygame.font.Font("freesansbold.ttf", 15)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((275),(25))
    gameDisplay.blit(TextSurf, TextRect)

def message_display5(text):
    #declares the font and font size 
    smallText = pygame.font.Font("freesansbold.ttf", 15)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((200),(300))
    gameDisplay.blit(TextSurf, TextRect)
    
def message_display6(text):
    #declares the font and font size 
    smallText = pygame.font.Font("freesansbold.ttf", 15)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((137),(350))
    gameDisplay.blit(TextSurf, TextRect)
    
def message_display7(text):
    #declares the font and font size 
    smallText = pygame.font.Font("freesansbold.ttf", 50)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)
    
def countdown():
    number = 3
    gameDisplay.fill(black)

    #numbers countdown from 1
    for i in range(3):
        message_display("GET READY")
        message_display1("Use the W , S keys to control paddle if you are Player 1.")
        message_display2("Use the UP , DOWN arrow keys to control paddle if you are player 2.")
        message_display5("Hit the ball with the paddle as it goes to your side.")
        message_display6("First to 10 points wins the game")
        
        wasd = gameDisplay.blit(wasdinstructions,(375,350))       
        pygame.display.update()
        number -= 1
        time.sleep(1)
        gameDisplay.fill(black)
 
    
#button function   
def button(msg, x, y, w, h, inactive_colour, active_colour, action, fontsize):

    #Defines mouse, as the coodinates of the mouse
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #checks if the mouse is within the coordinates of the button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        #draws the button in the active colour
        pygame.draw.rect(gameDisplay, active_colour, (x, y, w, h))
        #checks if the left mouse is pressed
        if click[0] == 1:
            #performs action based on the button's said function
            if action == "play":
                countdown()
                intro()
            if action == "instructions":
                instruction()
            if action == "quit":
                pygame.quit()
                quit()
            if action == "main_menu":
                main_menu()
            if action == "begin":
                gameLoop()
            if action == "OK":
                gameLoop()
    #if the mouse is not within the coordinates of the button, it draws the button in it's inactive colour
    else:
        pygame.draw.rect(gameDisplay, inactive_colour, (x, y, w, h))
    #draws text on the button
    smallText = pygame.font.Font("freesansbold.ttf", fontsize)
    textSurf, textRect = text_objects(msg, smallText)
    #Centers the text on the button
    textRect.center = ( (x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)

#______________________________________________________________________________________
#defines the main menu/lobby for the game
def main_menu():

    intro = True
    #creates loop for the game
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # draws background image
        gameDisplay.blit(background_level1, (0,0))
        gameDisplay.blit(background, (0, 0))
  
        message_display4("Game by: Evan Shizas, Mohammad-Ibrahim Yosufzay and Oscar Lam")
        #draws buttons
        button("Start Game", 300, 225, 125, 50, gray, light_gray, "play", 20) 
        button("Instructions", 300, 325, 125, 50, gray, light_gray, "instructions", 20)
        button("Quit Game", 300, 425, 125, 50, gray, light_gray, "quit", 20)                                 
        #updates the display
        pygame.display.flip()
        clock.tick(60)

#defines the instructions page        
def instruction():
    intro = True
    #creates a loop for the game
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #blits the background 
        
        gameDisplay.blit(instructions, (0, 0))
        #button to return to main menu
        message_display("How to Play")
        message_display1("Use the W , S keys to control paddle if you are Player 1.")
        message_display2("Use the UP , DOWN arrow keys to control paddle if you are player 2.")
        message_display5("Hit the ball with the paddle as it goes to your side.")
        message_display6("First to 10 points wins the game!")
        
        wasd = gameDisplay.blit(wasdinstructions,(375,350))
        button("Back", 0, 0, 125, 50, gray, light_gray, "main_menu", 40)

        #updates the display
        pygame.display.flip()
        clock.tick(60)
        
def intro():
    intro = True
    #creates a loop for the game
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
        #button to begin the game
        #button("OK", 500, 650, 150, 75, gray, light_gray, "begin", 40)
        
        ########################################################
        # Your working game should go here.
        
        # Import the pygame library and initialise the game engine
 
        from paddle import Paddle
        from ball import Ball
        
        pygame.init()
        
        # Define some colors
        BLACK = (0,0,0)
        WHITE = (255,255,255)
        
        # Open a new window
        size = (700, 500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Pong")
        
        paddleA = Paddle(WHITE, 10, 100)
        paddleA.rect.x = 20
        paddleA.rect.y = 200
        
        paddleB = Paddle(WHITE, 10, 100)
        paddleB.rect.x = 670
        paddleB.rect.y = 200
        
        ball = Ball(WHITE,10,10)
        ball.rect.x = 345
        ball.rect.y = 195
        
        #This will be a list that will contain all the sprites we intend to use in our game.
        all_sprites_list = pygame.sprite.Group()
        
        # Add the car to the list of objects
        all_sprites_list.add(paddleA)
        all_sprites_list.add(paddleB)
        all_sprites_list.add(ball)
        
        # The loop will carry on until the user exit the game (e.g. clicks the close button).
        carryOn = True
        
        # The clock will be used to control how fast the screen updates
        clock = pygame.time.Clock()
        
        #Initialise player scores
        scoreA = 0
        scoreB = 0
        
        # -------- Main Program Loop -----------
        while carryOn:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    carryOn = False # Flag that we are done so we exit this loop
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                        carryOn=False
        
            #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddleA.moveUp(8)
            if keys[pygame.K_s]:
                paddleA.moveDown(8)
            if keys[pygame.K_UP]:
                paddleB.moveUp(8)
            if keys[pygame.K_DOWN]:
                paddleB.moveDown(8)    
        
            # --- Game logic should go here
            all_sprites_list.update()
        
            #Check if the ball is bouncing against any of the 4 walls:
            if ball.rect.x>=690:
                scoreA+=1
                ball.rect.x = 345
                ball.rect.y = 195
                paddleB.rect.x = 670
                paddleB.rect.y = 200
                paddleA.rect.x = 20
                paddleA.rect.y = 200                
                time.sleep(1)
                ball.velocity[1]
            if ball.rect.x<=0:
                scoreB+=1
                ball.rect.x = 345
                ball.rect.y = 195
                paddleB.rect.x = 670
                paddleB.rect.y = 200
                paddleA.rect.x = 20
                paddleA.rect.y = 200                
                time.sleep(1)                
                ball.velocity[1]
            if ball.rect.y>490:
                ball.velocity[1] = -ball.velocity[1]
            if ball.rect.y<0:
                ball.velocity[1] = -ball.velocity[1]
                
        
            #Detect collisions between the ball and the paddles
            if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
                ball.bounce()

            # --- Drawing code should go here
            # First, clear the screen to black. 
            screen.fill(BLACK)
            #Draw the net
            pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        
            #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
            all_sprites_list.draw(screen) 
        
            #Display scores:
            font = pygame.font.Font(None, 74)
            text = font.render(str(scoreA), 1, WHITE)
            screen.blit(text, (200,10))
            text = font.render(str(scoreB), 1, WHITE)
            screen.blit(text, (470,10))
            
            if scoreA == 10:
                message_display3("Player 1 Wins!")
                main_menu()
                
            elif scoreB == 10:
                message_display3("Player 2 Wins!")
                main_menu()            
            
            #button to go back to main menu
            button("EXIT", 300, 0, 100, 30, gray, light_gray, "main_menu", 30)
            
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limits to 90 frames per second
            clock.tick(90)
            
        #Once we have exited the main program loop we can stop the game engine:
        pygame.quit()
        

        #button to return to main menu
        button("Back", 800, 650, 250, 100, gray, light_gray, "main_menu", 40)        
        
        #updates the display
        pygame.display.flip()
        clock.tick(60)
    

def gameLoop():

    gameExit = False
    #creates loop for the game
    while gameExit == False:
        main_menu()

gameLoop()