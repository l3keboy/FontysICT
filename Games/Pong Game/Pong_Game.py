import pygame
from random import randint
import time

# === COLORS === #
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# === INITIALIZE GAME === #
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([int(screen_width), int(screen_height)])
icon = pygame.image.load("Pong_icon.png")
pygame.display.set_caption("Pong Game by Luke")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


# === CLASSES === #
class PaddleWS(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        self.rect.y += int(pixels)
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += int(pixels)
        if self.rect.y > 550:
            self.rect.y = 550


class PaddleUpDown(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        self.rect.y += int(pixels)
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += int(pixels)
        if self.rect.y > 550:
            self.rect.y = 550


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        self.velocity = [randint(8, 12), randint(-8, 8)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)


# === FUNCTIONS === #
def dashed_line():
    d = 1
    for d in range(1, int((screen_height / 20) + 1)):
        dashed_line_y1 = (20 * d) - 20
        dashed_line_y2 = (20 * d) - 10
        pygame.draw.line(screen, WHITE, [400, dashed_line_y1], [400, dashed_line_y2], 3)
        d += 1


# === SPRITES INFO === #
all_sprites_list = pygame.sprite.Group()

paddle_left = PaddleWS(WHITE, 5, 50)
paddle_left.rect.x = 20
paddle_left.rect.y = 275

paddle_right = PaddleUpDown(WHITE, 5, 50)
paddle_right.rect.x = 780
paddle_right.rect.y = 275

ball1 = Ball(WHITE, 6, 6)
ball1.rect.x = int(screen_width / 2)
ball1.rect.y = int(screen_height / 2)

all_sprites_list.add(paddle_left)
all_sprites_list.add(paddle_right)
all_sprites_list.add(ball1)

score_left = 0
score_right = 0

# === GAME === #
game_close = True
while game_close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_close = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_left.move_up(-10)
    if keys[pygame.K_s]:
        paddle_left.move_down(10)
    if keys[pygame.K_UP]:
        paddle_right.move_up(-10)
    if keys[pygame.K_DOWN]:
        paddle_right.move_down(10)

    all_sprites_list.update()

    # Check if ball hits one of the wall, if sidewalls are hit add 1 to opponents score.
    if ball1.rect.x >= 800:
        score_right += 1
        ball1.rect.x = int(screen_width / 2)
        ball1.rect.y = int(screen_height / 2)
        ball1.velocity[0] = -ball1.velocity[0]
    if ball1.rect.x <= 0:
        score_left += 1
        ball1.rect.x = int(screen_width / 2)
        ball1.rect.y = int(screen_height / 2)
        ball1.velocity[0] = -ball1.velocity[0]
    if ball1.rect.y > 600:
        ball1.velocity[1] = -ball1.velocity[1]
    if ball1.rect.y < 0:
        ball1.velocity[1] = -ball1.velocity[1]

    # Check if ball and paddle collide.
    if pygame.sprite.collide_mask(ball1, paddle_left) or pygame.sprite.collide_mask(ball1, paddle_right):
        ball1.bounce()

    screen.fill(BLACK)
    dashed_line()

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    screen.blit(font.render(str(score_right), 1, WHITE), (200, 10))
    screen.blit(font.render(str(score_left), 1, WHITE), (600, 10))

    pygame.display.update()

    clock.tick(30)
