import pygame
import random #imported random for the random "cookies"

pygame.init()

# screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #same as before
# snake setup
snake_color = (255, 0, 0)  # red boyo
snake_size = 50  # size of each snake segment
snake_pos = [(300, 250)]  # initial position and length
direction = 'STOP'  # initial direction
# food setup
food_color = (0, 255, 0)  # green is not a creative color
food_size = 50 # try 500, it's kinda funny
food_pos = [random.randrange(0, SCREEN_WIDTH//food_size) * food_size,
            random.randrange(0, SCREEN_HEIGHT//food_size) * food_size]  # this is why we imported random. we set randrange for the cookies (food)
# This is the same as when we did player = from the program before.
def draw_snake():
    for pos in snake_pos:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

def move_snake():
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

    # new head and remove the last segment
    snake_pos.insert(0, new_head)
    if snake_pos[0] == food_pos:  # check if snake has eaten food (aka, if snake pos is equivalent to food pos)
        return snake_pos  # keep last segment IF we ate food
    else:
        snake_pos.pop()  # remove the last segment if we didn't eat food (this is the same from before)
    return snake_pos # add a return statement



run = True
clock = pygame.time.Clock()  # set up a game clock for controlling the frame rate (down below)

while run:
    screen.fill((0, 0, 0))  # clear the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # Same as before, quit game if pygame.Quit is true
        # input aka key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != 'DOWN': # same as before, but we put != statements for opposing directions, this stops from eating itself
                direction = 'UP'
            elif event.key == pygame.K_s and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_a and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_d and direction != 'LEFT':
                direction = 'RIGHT'
    move_snake() # calling the functions
    draw_snake() # calling the functions
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size)) # food

    # check for eating food
    if snake_pos[0] == food_pos:
        snake_pos.append(snake_pos[-1])  # snake grow
        food_pos = [random.randrange(0, SCREEN_WIDTH//food_size) * food_size,
                    random.randrange(0, SCREEN_HEIGHT//food_size) * food_size] 
        # snake no grow?

    pygame.display.update()  # update our display
    clock.tick(15)  # limit frame to 15 (i tried 60, it was not fun)

pygame.quit()


# Things to do:
# Better food collision 
# Snake growth
# Food regeneration


# Changelog: 
# Changed line 18/19 values to 0
# Added a check for snake pos
# Forgot to change bottom variables for food_pos, changed both to 0
# WHY SNAKE NO EAT