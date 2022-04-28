import pygame
import random

pygame.init()

snake_color = (25, 25, 77)
food_color = (179, 60, 0)
text_color = (255, 255, 128)
bg_color = (163, 163, 117)
window_width = 400
window_height = 300
snake_block = 10

dis = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Goes Yummy')


def draw_snake(snake):
    for i in snake:
        pygame.draw.rect(dis, (0, 77, 0), [i[0], i[1], snake_block, snake_block])
        pygame.draw.rect(dis, snake_color, [i[0] + 1, i[1] + 1, snake_block - 1, snake_block - 1])


def draw_message(msg, color, place, size):
    font_style = pygame.font.SysFont(None, size)
    m = font_style.render(msg, True, color)
    dis.blit(m, [place[0], place[1]])


def game():
    snake_x = int(window_width / 2)
    snake_y = int(window_height / 2)
    move_x = 0
    move_y = 0
    clock = pygame.time.Clock()
    food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
    snake_list = []
    snake_len = 1
    score = 0
    food_consumed = False
    running = True
    game_over_pause = False
    while running:
        while game_over_pause:
            draw_message("You Lost! Press 'R' to restart!", text_color, (10, 80), 35)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over_pause = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over_pause = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if move_x != snake_block:
                        move_x = -snake_block
                        move_y = 0
                elif event.key == pygame.K_RIGHT:
                    if move_x != -snake_block:
                        move_x = snake_block
                        move_y = 0
                elif event.key == pygame.K_UP:
                    if move_y != snake_block:
                        move_x = 0
                        move_y = -snake_block
                elif event.key == pygame.K_DOWN:
                    if move_y != -snake_block:
                        move_x = 0
                        move_y = snake_block

        snake_x += move_x
        snake_y += move_y
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_len:
            del snake_list[0]

        if food_consumed:
            food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            food_consumed = False

        for body_cell in snake_list[:-1]:
            if body_cell == snake_head:
                game_over_pause = True

        if snake_head[0] < 0 or snake_head[0] > window_width or snake_head[1] < 0 or snake_head[1] > window_height:
            game_over_pause = True

        dis.fill(bg_color)
        pygame.draw.rect(dis, food_color, [food_x, food_y, snake_block, snake_block])
        draw_snake(snake_list)
        draw_message("Your score: " + str(score), text_color, (10, 10), 30)
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            score += 100
            snake_len += 1
            food_consumed = True
        clock.tick(15)

    pygame.quit()
    quit()


game()
