#sprite
import pygame
import random
# 初始化
pygame.init()
# 设置窗口大小
FPS = 60;
White = (255, 255, 255)  
Width = 500
Height = 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("My Game")  
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # 填充顏色
        self.rect = self.image.get_rect()
        self.rect.x = (Width // 2) 
        self.rect.bottom = Height-10 # 設置初始位置
        self.speedx = 8
    def update(self):
        key_pressed = pygame.key.get_pressed()
        
        if key_pressed[pygame.K_d]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_a]:
            self.rect.x -= self.speedx
       
        if self.rect.right > Width:
            self.rect.right = Width 
        if self.rect.x < 0:
            self.rect.x = 0

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill((255, 0, 0))  # 填充顏色
        self.rect = self.image.get_rect()
        self.rect.x = (random.randrange(0, Width-30))
        self.rect.y = (random.randrange(-100, Height-40)) 
        self.speedy = random.randrange(2, 10)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        key_pressed = pygame.key.get_pressed()
        
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > Height or self.rect.left < 0 or self.rect.right > Width:
            self.rect.x = (random.randrange(0, Width-30))
            self.rect.y = (random.randrange(-100, Height-40)) 
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    rock = Rock()
    all_sprites.add(rock)


running = True





# 遊戲迴圈
while running:
    clock.tick(FPS)  # 控制幀率
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()  # 更新所有精靈的位置

    screen.fill(White);
    all_sprites.draw(screen)
    pygame.display.update();  

pygame.quit()