import pygame
import sys

class Coin:
    def __init__(self, image, position):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect.topleft)

    def move_to(self, position):
        self.rect.topleft = position

pygame.init()
print("Dessigned by Julian Kaints")

width, height = 750, 850
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PacMan')

pacman = pygame.image.load('pacman.png')
block1 = pygame.image.load('block1.png')
block2 = pygame.image.load('block2.png')
block3 = pygame.image.load('block3.png')
block4 = pygame.image.load('block4.png')
block5 = pygame.image.load('block5.png')
block6 = pygame.image.load('block6.png')
block7 = pygame.image.load('block7.png')
block8 = pygame.image.load('block8.png')
gage = pygame.image.load('gage.png')

ghost = pygame.image.load('ghost.png')
coin_image = pygame.image.load('coin.png')

coins = [
    Coin(coin_image, (120, 220)),
    Coin(coin_image, (620, 220)),
    Coin(coin_image, (120, 420)),
    Coin(coin_image, (620, 420)),
    Coin(coin_image, (370,720)),
]

pacman_rect = pacman.get_rect()
pacman_rect.topleft = (350, 300)

auto_speed = 2
manual_speed = 3
current_speed = [0, 0]

score = 0

won = False

blocks = [
    {"image": block3, "position": (50, 250)},
    {"image": block3, "position": (100, 250)},
    {"image": block3, "position": (50, 200)},
    {"image": block5, "position": (150, 250)},
    {"image": block4, "position": (50, 150)},
    {"image": block3, "position": (300, 250)},
    {"image": block3, "position": (350, 250)},
    {"image": block3, "position": (400, 250)},
    {"image": block5, "position": (450, 250)},
    {"image": block2, "position": (250, 250)},
    {"image": block3, "position": (350, 200)},
    {"image": block4, "position": (350, 150)},
    {"image": block2, "position": (550, 250)},
    {"image": block3, "position": (600, 250)},
    {"image": block3, "position": (650, 250)},
    {"image": block3, "position": (650, 200)},
    {"image": block3, "position": (650, 200)},
    {"image": block4, "position": (650, 150)},
    {"image": block3, "position": (50, 350)},
    {"image": block3, "position": (50, 400)},
    {"image": block3, "position": (100, 350)},
    {"image": block5, "position": (150, 350)},
    {"image": block6, "position": (50, 450)},
    {"image": block3, "position": (600, 350)},
    {"image": block3, "position": (650, 350)},
    {"image": block2, "position": (550, 350)},
    {"image": block3, "position": (650, 400)},
    {"image": block6, "position": (650, 450)},
    {"image": block1, "position": (150, 450)},
    {"image": block1, "position": (550, 450)},
    {"image": block2, "position": (50, 550)},
    {"image": block3, "position": (100, 550)},
    {"image": block3, "position": (150, 550)},
    {"image": block3, "position": (200, 550)},
    {"image": block5, "position": (250, 550)},
    {"image": block3, "position": (150, 600)},
    {"image": block6, "position": (150, 650)},
    {"image": block2, "position": (450, 550)},
    {"image": block3, "position": (500, 550)},
    {"image": block3, "position": (550, 550)},
    {"image": block3, "position": (600, 550)},
    {"image": block5, "position": (650, 550)},
    {"image": block3, "position": (550, 600)},
    {"image": block6, "position": (550, 650)},
    {"image": block4, "position": (50, 650)},
    {"image": block3, "position": (50, 700)},
    {"image": block3, "position": (50, 750)},
    {"image": block3, "position": (100, 750)},
    {"image": block5, "position": (150, 750)},
    {"image": block4, "position": (650, 650)},
    {"image": block3, "position": (650, 700)},
    {"image": block3, "position": (650, 750)},
    {"image": block3, "position": (600, 750)},
    {"image": block2, "position": (550, 750)},
    {"image": block4, "position": (350, 550)},
    {"image": block3, "position": (350, 600)},
    {"image": block3, "position": (350, 650)},
    {"image": block3, "position": (400, 650)},
    {"image": block7, "position": (450, 650)},
    {"image": block3, "position": (450, 700)},
    {"image": block6, "position": (450, 750)},
    {"image": block3, "position": (300, 650)},
    {"image": block8, "position": (250, 650)},
    {"image": block3, "position": (250, 700)},
    {"image": block6, "position": (250, 750)},
    {"image": block1, "position": (350, 750)},
    {"image": block2, "position": (150, 150)},
    {"image": block3, "position": (200, 150)},
    {"image": block5, "position": (250, 150)},
    {"image": block2, "position": (450, 150)},
    {"image": block3, "position": (500, 150)},
    {"image": block5, "position": (550, 150)},
    {"image": block2, "position": (50, 50)},
    {"image": block3, "position": (100, 50)},
    {"image": block5, "position": (150, 50)},
    {"image": block2, "position": (250, 50)},
    {"image": block3, "position": (300, 50)},
    {"image": block3, "position": (350, 50)},
    {"image": block3, "position": (400, 50)},
    {"image": block5, "position": (450, 50)},
    {"image": block2, "position": (550, 50)},
    {"image": block3, "position": (600, 50)},
    {"image": block5, "position": (650, 50)},
]

ghost_rect = ghost.get_rect()
ghost_rect.topleft = (300, 400)
ghost_speed = 2  

clock = pygame.time.Clock()

def is_valid_move(rect, direction, speed):
    test_rect = rect.copy()
    if direction == "UP":
        test_rect.y -= speed
    elif direction == "DOWN":
        test_rect.y += speed
    elif direction == "LEFT":
        test_rect.x -= speed
    elif direction == "RIGHT":
        test_rect.x += speed

    for block in blocks:
        block_rect = block["image"].get_rect(topleft=block["position"])
        if test_rect.colliderect(block_rect):
            return False

    return True

def game_over():
    print("Game Over!")
    pygame.quit()
    sys.exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    for coin in coins:
        if pacman_rect.colliderect(coin.rect) and not coin.collected:
            coin.collected = True
            score += 1
            print(score, "/5 coins collected")
            
    if score == 5 and not won:
        ghost_speed = 0
        manual_speed = 0
        print("You Won!")
        won = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if is_valid_move(pacman_rect, "UP", manual_speed):
            current_speed = [0, -manual_speed]
    elif keys[pygame.K_DOWN]:
        if is_valid_move(pacman_rect, "DOWN", manual_speed):
            current_speed = [0, manual_speed]
    elif keys[pygame.K_LEFT]:
        if is_valid_move(pacman_rect, "LEFT", manual_speed):
            current_speed = [-manual_speed, 0]
    elif keys[pygame.K_RIGHT]:
        if is_valid_move(pacman_rect, "RIGHT", manual_speed):
            current_speed = [manual_speed, 0]

    pacman_rect.x += current_speed[0]
    pacman_rect.y += current_speed[1]

    pacman_rect.x = max(0, min(width - pacman_rect.width, pacman_rect.x))
    pacman_rect.y = max(0, min(height - pacman_rect.height, pacman_rect.y))

    if ghost_rect.colliderect(pacman_rect):
        game_over()  

    if ghost_rect.x < pacman_rect.x and is_valid_move(ghost_rect, "RIGHT", ghost_speed):
        ghost_rect.x += ghost_speed
    elif ghost_rect.x > pacman_rect.x and is_valid_move(ghost_rect, "LEFT", ghost_speed):
        ghost_rect.x -= ghost_speed

    if ghost_rect.y < pacman_rect.y and is_valid_move(ghost_rect, "DOWN", ghost_speed):
        ghost_rect.y += ghost_speed
    elif ghost_rect.y > pacman_rect.y and is_valid_move(ghost_rect, "UP", ghost_speed):
        ghost_rect.y -= ghost_speed

    for block in blocks:
        block_rect = block["image"].get_rect(topleft=block["position"])
        if pacman_rect.colliderect(block_rect):
            if current_speed[0] > 0:
                pacman_rect.right = block_rect.left
            elif current_speed[0] < 0:
                pacman_rect.left = block_rect.right
            if current_speed[1] > 0:
                pacman_rect.bottom = block_rect.top
            elif current_speed[1] < 0:
                pacman_rect.top = block_rect.bottom

    screen.fill((0))
    screen.blit(pacman, pacman_rect)
    screen.blit(gage, (250, 350))
    screen.blit(ghost, ghost_rect)

    for coin in coins:
        coin.draw(screen)

    for block in blocks:
        screen.blit(block["image"], block["position"])

    pygame.display.update()
    clock.tick(60)
