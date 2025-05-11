#sprite
import pygame

# 初始化
pygame.init()
# 设置窗口大小
FPS = 60;
White = (255, 255, 255)  
Width = 800
Height = 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("My Game")  
clock = pygame.time.Clock()

running = True;


# 遊戲迴圈
while running:
    clock.tick(FPS)  # 控制幀率
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(White);
    pygame.display.update();  

pygame.quit()