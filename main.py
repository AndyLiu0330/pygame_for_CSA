import pygame
import random
import os 
# 初始化
pygame.init()

# 設定參數
FPS = 60
White = (0,0, 0)
Width = 500
Height = 600
score = 0
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


# 載入圖片
backgroundImg = pygame.image.load(os.path.join("img", "background.png")).convert()
playerImg = pygame.image.load(os.path.join("img", "player.png")).convert()
rockImg = pygame.image.load(os.path.join("img", "rock.png")).convert()
bulletImg = pygame.image.load(os.path.join("img", "bullet.png")).convert()
rockImgs = []
for i in range(7):
    rockImgs.append(pygame.image.load(os.path.join("img",f"rock{i}.png")).convert())
fontName = pygame.font.match_font("arial")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

# 玩家類
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.transform.scale (playerImg, (50, 38))
        self.image.set_colorkey(White)
      
        self.rect = self.image.get_rect()
        self.rect.x = Width // 2
        self.rect.bottom = Height - 10
        self.radius = self.rect.width *0.9 // 2

        self.speedx = 8

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_a]:
            self.rect.x -= self.speedx
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = self.Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    # 內部定義 Bullet 類
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = bulletImg
            self.image.set_colorkey(White)
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.y = y
            self.speedy = -10

        def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom < 0:
                self.kill()

# 石頭類  
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageO = random.choice(rockImgs)
        self.image = self.imageO.copy()
        self.image.set_colorkey(White)
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, Width - 30)
        self.rect.y = random.randrange(-180,  -100)
        self.radius = int (self.rect.width *0.9// 2)
        self.speedy = random.randrange(2, 10)
        self.speedx = random.randrange(-3, 3)
        self.totalDegree = 0
        self.degree = random.randrange(-3, 3)


    def rotate(self):
        self.totalDegree += self.degree
        self.totalDegree = self.totalDegree %360
        self.image = pygame.transform.rotate(self.imageO, self.degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rent.center = center
        
        
        
    def update(self):
    
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > Height or self.rect.left < 0 or self.rect.right > Width:
            self.rect.x = random.randrange(0, Width - 30)
            self.rect.y = random.randrange(-180,  -100)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)

# 精靈組
bullets = pygame.sprite.Group()
rocks = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)

# 遊戲迴圈
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.shoot()



    all_sprites.update()
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
    for hit in hits:
        score += hit.radius
        rock = Rock()
        all_sprites.add(rock)
        rocks.add(rock)
    
    hits = pygame.sprite.spritecollide(player, rocks, False, pygame.sprite.collide_circle)
    if hits:
        running = False        


    screen.fill(White)
    screen.blit(backgroundImg, (0, 0))
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, Width // 2, 10)
    pygame.display.update()

pygame.quit()