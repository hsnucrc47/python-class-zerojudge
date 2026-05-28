import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame-ce Sprite 架構 + 碰撞系統")

clock = pygame.time.Clock()
FPS = 60

# =========================================================
# ===== 子彈 =====
# =========================================================
#######
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("image/bullet.png")
        self.size = 10
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = -10

    def update(self, keys, events):
        self.rect.y += self.speed

        # 超出畫面就刪除
        if self.rect.bottom < 0:
            self.kill()
#######

# ===== 玩家 =====
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("image/player.png")
        self.size = 50
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        self.speed = 5

        #######
        self.hp = 5
        self.cooldown = 0
        #######

    def handle_input(self, keys, events):

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    #######
                    if self.cooldown == 0:
                        bullet = Bullet(self.rect.centerx, self.rect.top)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        self.cooldown = 15
                    #######

    def update(self, keys, events):

        self.handle_input(keys, events)

        #######
        if self.cooldown > 0:
            self.cooldown -= 1
        #######

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0


# ===== 敵人 =====
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("image/enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self, keys, events):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.rect.bottom = 0


# ===== 群組管理 =====
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(10):
    enemy = Enemy(i * 80, random.randint(-200, 0))
    all_sprites.add(enemy)
    enemies.add(enemy)


# ===== Game Over =====
#######
game_over = False
font = pygame.font.SysFont(None, 80)
#######

# ===== 主迴圈 =====
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:

        all_sprites.update(keys, events)

        # =====================================================
        # ===== 子彈打敵人（碰撞） =====
        # =====================================================
        #######
        hits = pygame.sprite.groupcollide(bullets, enemies, True, True)

        for hit in hits:
            print("擊中敵人！")
        #######

        # =====================================================
        # ===== 玩家撞敵人（扣血） =====
        # =====================================================
        #######
        if pygame.sprite.spritecollide(player, enemies, True):
            player.hp -= 1
            print("玩家受傷！HP:", player.hp)
        #######

        # =====================================================
        # ===== Game Over 判斷 =====
        # =====================================================
        #######
        if player.hp <= 0:
            game_over = True
        #######

    # ===== 畫面 =====
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # =====================================================
    # ===== UI 顯示 =====
    # =====================================================
    #######
    hp_text = font.render(f"HP: {player.hp}", True, (255, 255, 255))
    screen.blit(hp_text, (10, 10))
    #######

    # =====================================================
    # ===== Game Over 畫面 =====
    # =====================================================
    #######
    if game_over:
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (WIDTH//2 - 200, HEIGHT//2 - 50))
    #######

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()