import pygame
import random
        
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 460

display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Snake')

game_clock = pygame.time.Clock()

position_of_snake = [100, 50]
    
body_of_snake = [position_of_snake]
    
position_of_fruit = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]  
spawning_of_fruit = True
    
initial_direction = 'RIGHT'
snake_direction = initial_direction
speed_of_snake = 10

game_run = True
    
while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = 'UP'
            if event.key == pygame.K_DOWN:
                snake_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                snake_direction = 'RIGHT'
    
    if snake_direction == 'UP' and initial_direction != 'DOWN':
        initial_direction = 'UP'
    if snake_direction == 'DOWN' and initial_direction != 'UP':
        initial_direction = 'DOWN'   
    if snake_direction == 'LEFT' and initial_direction != 'RIGHT':
        initial_direction = 'LEFT'   
    if snake_direction == 'RIGHT' and initial_direction != 'LEFT':
        initial_direction = 'RIGHT'
    
    if initial_direction == 'UP':
        position_of_snake[1] -= 10
    if initial_direction == 'DOWN':
        position_of_snake[1] += 10
    if initial_direction == 'LEFT':
        position_of_snake[0] -= 10
    if initial_direction == 'RIGHT':
        position_of_snake[0] += 10
        
    body_of_snake.insert(0, list(position_of_snake))
    if position_of_snake[0] == position_of_fruit[0] and position_of_snake[1] == position_of_fruit[1]:
        spawning_of_fruit = False
    else:
        body_of_snake.pop()
    
    if not spawning_of_fruit:
        position_of_fruit = [
            random.randrange(1, (SCREEN_WIDTH//10)) * 10,
            random.randrange(1, (SCREEN_HEIGHT//10)) * 10
        ]
    spawning_of_fruit = True
    
    display_screen.fill("black")
    
    for position in body_of_snake:
        pygame.draw.rect(display_screen, (124, 252, 0), pygame.Rect(position[0], position[1], 10, 10))
        pygame.draw.rect(display_screen, (255, 69, 0), pygame.Rect(position_of_fruit[0], position_of_fruit[1], 10, 10))
    
    if position_of_snake[0] < 0 or position_of_snake[0] > SCREEN_WIDTH - 10:
        exit()
    if position_of_snake[1] < 0 or position_of_snake[1] > SCREEN_HEIGHT - 10:
        exit()
    
    for block in body_of_snake[1:]:
        if position_of_snake[0] == block[0] and position_of_snake[1] == block[1]:
            exit()
    
    pygame.display.update()
    
    game_clock.tick(speed_of_snake)
    
pygame.quit()