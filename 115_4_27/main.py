import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("輸入控制")

clock = pygame.time.Clock()
FPS = 60

class Player:
    def __init__(self):
        self.image = pygame.image.load("image/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = 100
        self.y = 100
        self.speed = 5

    def handle_input(self, keys, events):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("發射！")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

player = Player()

running = True

while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.handle_input(keys, events)

    screen.fill((0, 0, 0))
    player.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()