import pygame
import random

pygame.init()

# Colors
color_1 = (0, 0, 0)
color_2 = (0, 255, 0)
color_3 = (0, 200, 0)
color_4 = (255, 0, 0)
color_5 = (255, 255, 255)
color_6 = (0, 0, 0)

# Screen
box_len = 900
box_height = 600
screen = pygame.display.set_mode((box_len, box_height))
pygame.display.set_caption("SNAKE GAME")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font = pygame.font.SysFont("arial", 30, True)
score_font = pygame.font.SysFont("arial", 45, True)


def final_score(score):
    value = score_font.render(f"Score : {score}", True, color_2)
    screen.blit(value, [10, 10])


def make_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, color_3, [x[0], x[1], snake_block, snake_block])


def display_msg(msg, color):
    message = font.render(msg, True, color)
    screen.blit(message, [box_len / 6, box_height / 3])


def game_start():
    game_over = False
    game_close = False

    x1 = box_len / 2
    y1 = box_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_len = 1

    foodx = round(random.randrange(0, box_len - snake_block) / 10) * 10
    foody = round(random.randrange(0, box_height - snake_block) / 10) * 10

    while not game_over:

        while game_close:
            screen.fill(color_6)
            display_msg("You Lost! Press S-Play Again or E-Exit", color_4)
            final_score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_s:
                        game_start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= box_len or x1 < 0 or y1 >= box_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(color_6)
        pygame.draw.rect(screen, color_5, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_len:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        make_snake(snake_block, snake_list)
        final_score(snake_len - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, box_len - snake_block) / 10) * 10
            foody = round(random.randrange(0, box_height - snake_block) / 10) * 10
            snake_len += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_start()
