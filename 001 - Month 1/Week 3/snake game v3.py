import pygame
import random

pygame.init()

# screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# snek setup
snake_color = (255, 0, 0)  # green boyo
snake_size = 50  # make him small
snake_pos = [(300, 250)]  # initial position and length
direction = 'STOP'  # onitial direction
# food setup
food_color = (0, 255, 0)  # swapped to make it an apple
food_size = 50  # try 500, ^^ food size
food_pos = [random.randrange(0, SCREEN_WIDTH // food_size) * food_size,
            random.randrange(0, SCREEN_HEIGHT // food_size) * food_size]
# Same as before; nothing changed here
def draw_snake():
    for pos in snake_pos:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

def move_snake():
    global direction  # we made direction a global variable. this is to fix the issue of the food (now an apple) not being registered by the snake
    if direction == 'UP':
        new_head = (snake_pos[0][0], snake_pos[0][1] - snake_size)
    elif direction == 'DOWN':
        new_head = (snake_pos[0][0], snake_pos[0][1] + snake_size)
    elif direction == 'LEFT':
        new_head = (snake_pos[0][0] - snake_size, snake_pos[0][1])
    elif direction == 'RIGHT':
        new_head = (snake_pos[0][0] + snake_size, snake_pos[0][1])
    else:
        return

    # new head
    snake_pos.insert(0, new_head)
    # Check if snake has eaten food
    if snake_pos[0] == food_pos:
        return  # Do not remove the last segment
    snake_pos.pop()  # Remove the last segment
 #removed return statement in account to new globbal variable




run = True
clock = pygame.time.Clock() # frame rate will be below, as before

while run:
    screen.fill((0, 0, 0)) # clear the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # Same as before, wquit game if pygame.Quit is true
        # inputs for our key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != 'DOWN': # != (direction) invalidates oposing movements
                direction = 'UP'
            elif event.key == pygame.K_s and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_a and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_d and direction != 'LEFT':
                direction = 'RIGHT'

    move_snake() # Calling functions
    draw_snake() # Calling fucntions
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size)) #food

    # ff food is eaten, generate new food position and grow snake
    if snake_pos[0] == food_pos:
        food_pos = [random.randrange(0, SCREEN_WIDTH // food_size) * food_size,
                    random.randrange(0, SCREEN_HEIGHT // food_size) * food_size]

    pygame.display.update() # update our display
    clock.tick(15) # framerate (15 is good)

pygame.quit()




# Things to do:
# Better food collision 
# Snake growth
# Food regeneration
# Make a border
# Fix food again

# Changelog: 
# Changed line 18/19 values to 0
# Added a check for snake pos
# Forgot to change bottom variables for food_pos, changed both to 0
# WHY SNAKE NO EAT
# changed to global variable
# removed return statement in line 45
# nothing worked yet