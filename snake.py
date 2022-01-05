import pygame
import time
import random

pygame.init()

# Colors
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
yellow = (255, 255, 0)
grey = (100, 100, 100)

# Sizes
width = 300
height = 300

# Screen
display = pygame.display.set_mode((width, height))

# Time
clock = pygame.time.Clock()

# Snake's values
block = 10
snake_speed = 20

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
font_score = pygame.font.SysFont("bahnschrift", 35)

# Score
def Your_score(score):
    value = font_score.render("Ton score: " + str(score), True, yellow)
    display.blit(value, [0, 0])

# Snake
def our_snake(block, snake_size):
    for x in snake_size:
        pygame.draw.rect(display, green, [x[0], x[1], block, block])

# Game over message
def message(msg, color):
    msg = font_style.render(msg, True, color)
    display.blit(msg, [width / 6, height / 3])

# Game
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_size = []
    Length_of_snake = 1

    # Random food
    x_food = round(random.randrange(0, width - block) / 10.0) * 10.0
    y_food = round(random.randrange(0, height - block) / 10.0) * 10.0
    
    #Random rock
    x_rock = round(random.randrange(0, width - block) / 10.0) * 10.0
    y_rock = round(random.randrange(0, height - block) / 10.0) * 10.0

    while not game_over:
        
        while game_close == True:
            # background color
            display.fill(black)
            # game over message
            message("Tu as perdu !", yellow)
            # score without snake head
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            # game over events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_RETURN:
                        gameLoop()
        # game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # left
                # snake cannot go to the reverse side
                if event.key == pygame.K_LEFT and x1_change != block:
                    x1_change = -block
                    y1_change = 0
                # right
                if event.key == pygame.K_RIGHT and x1_change != -block:
                    x1_change = block
                    y1_change = 0
                # up
                if event.key == pygame.K_UP and y1_change != block:
                    y1_change = -block
                    x1_change = 0
                # down
                if event.key == pygame.K_DOWN and y1_change != -block:
                    y1_change = block
                    x1_change = 0
        # borders
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            pygame.mixer.music.load('sounds/zemmour.ogg')
            pygame.mixer.music.play()
            game_close = True
        x1 += x1_change
        y1 += y1_change
        #background color
        display.fill(black)
        # food spawn
        pygame.draw.rect(display, red, [x_food, y_food, block, block])
        #rock spawn
        pygame.draw.rect(display, grey, [x_rock, y_rock, block, block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_size.append(snake_Head)
        if len(snake_size) > Length_of_snake:
            del snake_size[0]
            
        # if snake hit itself
        for x in snake_size[:-1]:
            if x == snake_Head:
                pygame.mixer.music.load('sounds/zemmour.ogg')
                pygame.mixer.music.play()
                game_close = True

        our_snake(block, snake_size)
        Your_score(Length_of_snake - 1)

        pygame.display.update()
        # grow snake at every round if food is eaten
        if x1 == x_food and y1 == y_food:
            x_food = round(random.randrange(0, width - block) / 10.0) * 10.0
            y_food = round(random.randrange(0, height - block) / 10.0) * 10.0
            Length_of_snake += 1
            # same for rocks
            x_rock = round(random.randrange(0, width - block) / 10.0) * 10.0
            y_rock = round(random.randrange(0, height - block) / 10.0) * 10.0
            
            # pick random file
            sound = random.choice(["KK_Howl_c5.ogg", "KK_Me_a2.ogg", "KK_Me_c3.ogg", "KK_Na_c3.ogg", "KK_No_c3.ogg", "KK_Oh_a2.ogg", "KK_oo_c3.ogg", "KK_Way_c3.ogg", "KK_Whistle_g5.ogg"])
            # play sound
            pygame.mixer.music.load('sounds/' + sound)
            pygame.mixer.music.play()
            
        # if snake hit rock
        if x1 == x_rock and y1 == y_rock:
            x_rock = round(random.randrange(0, width - block) / 10.0) * 10.0
            y_rock = round(random.randrange(0, height - block) / 10.0) * 10.0
            pygame.mixer.music.load('sounds/zemmour.ogg')
            pygame.mixer.music.play()
            game_close = True
        
        # clock
        clock.tick(snake_speed)
    pygame.quit()
    quit()


gameLoop()