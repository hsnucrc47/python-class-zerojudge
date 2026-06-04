import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Final Demo")

clock = pygame.time.Clock()
FPS = 60

# ===== 字體 =====
font = pygame.font.Font("font/Cubic_11.ttf", 36)
big_font = pygame.font.Font("font/Cubic_11.ttf", 72)

# ===== 音效 =====
shoot_sound = pygame.mixer.Sound("sound/shoot.ogg")
hit_sound = pygame.mixer.Sound("sound/hit.wav")

# ===== 背景音樂 =====
pygame.mixer.music.load("sound/bgm.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 255, 0))

        self.rect = self.image.get_rect(center=(x, y))

        self.speed = -10

    def update(self):
        self.rect.y += self.speed

        if self.rect.bottom < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load(
            "image/explosion.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (64, 64)
        )

        self.rect = self.image.get_rect(center=pos)

        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.spawn_time > 300:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            "image/player.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (50, 50)
        )

        self.rect = self.image.get_rect(
            center=(WIDTH//2, HEIGHT-80)
        )

        self.speed = 5
        self.hp = 5

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(screen.get_rect())


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            "image/enemy.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (50, 50)
        )

        self.rect = self.image.get_rect(
            center=(random.randint(50, 750), -50)
        )

        self.speed = random.randint(2, 5)

    def update(self):

        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()


all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
effects = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

enemy_spawn_timer = 0
running = True
game_over = False

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    bullet = Bullet(
                        player.rect.centerx,
                        player.rect.top
                    )

                    all_sprites.add(bullet)
                    bullets.add(bullet)

                    shoot_sound.play()

    if not game_over:

        enemy_spawn_timer += 1

        if enemy_spawn_timer > 40:

            enemy_spawn_timer = 0

            enemy = Enemy()

            all_sprites.add(enemy)
            enemies.add(enemy)

        all_sprites.update()

        hits = pygame.sprite.groupcollide(
            bullets,
            enemies,
            True,
            True
        )

        for bullet, enemy_list in hits.items():

            hit_sound.play()

            for enemy in enemy_list:

                explosion = Explosion(
                    enemy.rect.center
                )

                all_sprites.add(explosion)
                effects.add(explosion)

        if pygame.sprite.spritecollide(
            player,
            enemies,
            True
        ):

            player.hp -= 1

        if player.hp <= 0:
            game_over = True

    screen.fill((20, 20, 20))

    all_sprites.draw(screen)

    hp_text = font.render(
        f"HP: {player.hp}",
        True,
        (255,255,255)
    )

    screen.blit(hp_text, (10, 10))

    if game_over:

        game_over_text = big_font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        screen.blit(
            game_over_text,
            (
                WIDTH//2 - game_over_text.get_width()//2,
                HEIGHT//2 - game_over_text.get_height()//2
            )
        )

    pygame.display.flip()

pygame.quit()