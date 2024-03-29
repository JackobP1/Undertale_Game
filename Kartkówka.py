import pygame
import random
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Delta")

# Postać gracza
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\JakubWolski\Desktop\game\images\heart.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.lives = 3  # liczba żyć gracza
        self.last_position = self.rect.center  # ostatnia znana lokalizacja gracza

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:  # Nie wychodź poza lewą krawędź
            self.rect.x -= 8
        elif keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:  # Nie wychodź poza prawą krawędź
            self.rect.x += 8
# Przeszkody
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\JakubWolski\Desktop\game\images\bone.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 80))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = -10
        self.speed_y = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = -10
            self.speed_y = random.randint(2, 6)

# Tekst punktacji
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Grupa dla przeszkód
obstacles = pygame.sprite.Group()

# Grupa dla gracza
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Czas trwania gry
clock = pygame.time.Clock()
game_over = False
start_time = pygame.time.get_ticks() // 1000

# Główna pętla gry
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Dodaj przeszkody
    if random.randint(1, 300) < 5:
        obstacle = Obstacle()
        obstacles.add(obstacle)
        all_sprites.add(obstacle)

    # Update
    all_sprites.update()

    # Sprawdź kolizje
    collision = pygame.sprite.spritecollide(player, obstacles, False)
    if collision:
        player.lives -= 1
        if player.lives == 0:
            game_over = True
        else:
            # Jeśli gracz stracił życie, przywróć jego ostatnią lokalizację
            player.rect.center = player.last_position
        # Rozbij obiekt gracza
        for obstacle in collision:
            obstacle.rect.y = SCREEN_HEIGHT + 100  # Przenieś przeszkodę poza ekran
            # Tutaj możesz dodać efekt rozpadu obiektu gracza

    # Zapisz aktualną lokalizację gracza
    player.last_position = player.rect.center

    # Wyczyszczenie ekranu
    SCREEN.fill((0, 0, 0))

    # Narysuj wszystkie obiekty
    all_sprites.draw(SCREEN)

    # Narysuj tekst z liczbą żyć
    draw_text(SCREEN, "Lives: {}".format(player.lives), 24, SCREEN_WIDTH // 2, 10)

    # Obliczanie czasu gry
    current_time = pygame.time.get_ticks() // 1000
    elapsed_time = current_time - start_time
    draw_text(SCREEN, "Time: {}s".format(elapsed_time), 24, SCREEN_WIDTH // 2, 40)

    # Odświeżenie ekranu
    pygame.display.flip()

    # Ustawienia czasu
    clock.tick(60)

pygame.qui

