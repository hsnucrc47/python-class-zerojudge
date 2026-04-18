import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite 架構")

clock = pygame.time.Clock()
FPS = 60

# ===== Sprite 基底類別 =====
class Sprite:
    def update(self, keys, events):
        pass

    def draw(self, screen):
        pass


# ===== 玩家 =====
class Player(Sprite):
    def __init__(self):
        self.image = pygame.image.load("image/player.png")
        self.size = 50
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.x = 100
        self.y = 100
        self.speed = 5

    def handle_input(self, keys, events):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("發射！")

    def update(self, keys, events):
        self.handle_input(keys, events)
        if self.y > HEIGHT - self.size:
            self.y = HEIGHT - self.size
        if self.x > WIDTH - self.size:
            self.x = WIDTH - self.size
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# ===== 敵人 =====
class Enemy(Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("image/enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = x
        self.y = y
        self.speed = 2

    def update(self, keys, events):
        self.y += self.speed  # 自動往下移動
        if self.y > HEIGHT:
            self.y = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# ===== 建立所有物件 =====
sprites = []

player = Player()
sprites.append(player)

# 建立多個敵人
for i in range(10):
    enemy = Enemy(i * 80, 0)
    sprites.append(enemy)


# ===== 主迴圈 =====
running = True

while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # ===== 更新所有物件 =====
    for s in sprites:
        s.update(keys, events)

    # ===== 繪製 =====
    screen.fill((0, 0, 0))

    for s in sprites:
        s.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()