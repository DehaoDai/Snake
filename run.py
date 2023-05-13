import pygame
import random

# 初始化游戏
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义蛇的初始位置和大小
snake_size = 20
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_x_change = 0
snake_y_change = 0

# 定义食物的初始位置和大小
food_size = 20
food_x = round(random.randrange(0, screen_width - food_size) / 20) * 20
food_y = round(random.randrange(0, screen_height - food_size) / 20) * 20

# 定义得分
score = 0
font = pygame.font.SysFont(None, 30)

# 定义游戏结束标志
game_over = False

clock = pygame.time.Clock()

# 定义蛇的移动函数
def snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_size, snake_size])

# 游戏主循环
snake_list = []
snake_length = 1
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_size
                snake_x_change = 0

    # 更新蛇的位置
    snake_x += snake_x_change
    snake_y += snake_y_change

    # 边界碰撞检测
    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        game_over = True

    # 画蛇和食物
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [food_x, food_y, food_size, food_size])
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    snake(snake_size, snake_list)

    # 蛇吃食物
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, screen_width - food_size) / 20)
        food_y = round(random.randrange(0, screen_height - food_size) / 20) * 20
        snake_length += 1
        score += 1

    # 显示得分
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

    # 更新屏幕
    pygame.display.update()

    # 控制游戏帧率
    clock.tick(10)  # 控制蛇的移动速度

# 游戏结束后显示最终得分
game_over_text = font.render("Game Over! Final Score: " + str(score), True, WHITE)
screen.blit(game_over_text, [screen_width / 2 - 100, screen_height / 2])
pygame.display.update()

# 停留2秒后退出游戏
pygame.time.wait(2000)

# 退出游戏
pygame.quit()

