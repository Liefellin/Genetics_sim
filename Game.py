# Import and initialize the pygame library
import pygame
import random
from pygame.locals import *
pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])

adam_image = pygame.image.load("Sample_Tribble.gif")
field = pygame.image.load("field.gif")
FPS = 60
FramePerSec = pygame.time.Clock()


class Tribble(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.image = adam_image
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)
        self.name = name
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(random.choice([0, 10, -10]), random.choice([0, 10]))

        if self.rect.center[1] > 1000:

            self.rect.center = (self.rect.center[0], 0)


Tribble1 = Tribble("Adam")

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # if TribInst.collidepoint(event.pos):
                pass
    Tribble1.move()
    screen.blit(field, (0,0))
    Tribble1.draw(screen)
    pygame.display.update()
    FramePerSec.tick(FPS)
# Done! Time to quit.
pygame.quit()
