import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("我的遊戲")

clock = pygame.time.Clock()
FPS = 60

# 定義類別 Player
class Player:
    def __init__(self):
        self.image = pygame.image.load("image/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = 100
        self.y = 100

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_UP]:
            self.y -= 5
        if keys[pygame.K_DOWN]:
            self.y += 5

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

player = Player()

running = True

while running:
    for event in pygame.event.get():
        # 關閉視窗
        if event.type == pygame.QUIT:
            running = False
    
    # 觸發按鍵
    keys = pygame.key.get_pressed()
    player.move(keys)

    # 畫背景、角色
    screen.fill((0, 0, 0))
    player.draw(screen)
    
    # 更新畫面、幀數
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()