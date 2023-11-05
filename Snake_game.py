import pygame
import random

# Initialize the game
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake and food
snake = [(200, 200)]
snake_length = 1
direction = (1, 0)
food_pos = (random.randrange(1, (screen_width // 10)) * 10, random.randrange(1, (screen_height // 10)) * 10)
score = 0
speed = 15

# Game over function
def game_over():
    font = pygame.font.SysFont('Arial', 60)
    text = font.render(f'Game Over! Your score: {score}', True, red)
    screen.blit(text, (screen_width / 6, screen_height / 3))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

# Main game logic
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    head = (snake[0][0] + direction[0] * 10, snake[0][1] + direction[1] * 10)
    snake.insert(0, head)

    if snake[0] == food_pos:
        food_pos = (random.randrange(1, (screen_width // 10)) * 10, random.randrange(1, (screen_height // 10)) * 10)
        score += 10
        speed += 1
    else:
        snake.pop()

    if (
        snake[0][0] not in range(0, screen_width)
        or snake[0][1] not in range(0, screen_height)
        or snake.count(snake[0]) > 1
    ):
        game_over()

    screen.fill(black)
    for pos in snake:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Display score
    font = pygame.font.SysFont('Arial', 30)
    score_text = font.render(f'Score: {score}', True, red)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(speed)
