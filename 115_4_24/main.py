import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame-ce Sprite 架構")

clock = pygame.time.Clock()
FPS = 60

# ===== 玩家 =====
# 1. 繼承 pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # 必須呼叫父類別初始化
        # 載入圖片並設定
        self.image = pygame.image.load("image/player.png").convert_alpha()
        self.size = 50
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        
        # 2. 正統做法：使用 rect 管理位置
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        self.speed = 5

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
                    print("發射！")

    def update(self, keys, events):
        self.handle_input(keys, events)

        # 3. 使用 rect 的屬性來處理邊界問題
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
        self.image = pygame.image.load("image/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    # 為了保持 Group.update 能運作，參數必須與 Player 一致即使不會用到
    def update(self, keys, events):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

# ===== 建立與管理精靈 =====
# 使用 Group 建立 all_sprites
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 建立多個敵人並加入群組
for i in range(10):
    enemy = Enemy(i * 80, 0)
    all_sprites.add(enemy)

# ===== 主迴圈 =====
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # ===== 更新與繪製 (正統語法) =====
    
    # 呼叫 Group 的 update，它會自動呼叫裡面所有 Sprite 的 update
    all_sprites.update(keys, events)

    screen.fill((0, 0, 0))

    # 一行程式碼搞定繪製
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()