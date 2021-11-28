import pygame  # Import library
import random  # Import library

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Snake Game by Luke")
font_style = pygame.font.SysFont("impact", 50)
score_font = pygame.font.SysFont("comicsansms", 20)

clock = pygame.time.Clock()


def message(msg, color, loc_x, loc_y):
    show_message = font_style.render(msg, True, color)
    screen.blit(show_message, [loc_x, loc_y])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLUE, [x[0], x[1], snake_block, snake_block])


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, YELLOW)
    screen.blit(value, [0, 0])


def game():
    # === GAME === #
    game_over = False
    game_close = False

    snake_block = 10
    snake_speed = 15
    # === SPRITES === #
    start_x = screen_width / 2
    start_y = screen_height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length_snake = 1

    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Press Q to quit or press R to retry", WHITE, 70, 350)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block

        if start_x >= screen_width or start_x < 0 or start_y >= screen_height or start_y < 0:
            game_close = True
        start_x += x_change
        start_y += y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [int(food_x), int(food_y), snake_block, snake_block])

        snake_head = [start_x, start_y]
        snake_list.append(snake_head)

        if len(snake_list) > length_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_snake - 1)

        pygame.display.update()

        if start_x == food_x and start_y == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            length_snake += 1
            if snake_speed < 30:
                snake_speed += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game()
