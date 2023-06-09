import random
import pygame.sprite


class Mouse(pygame.sprite.Sprite):
    move_speed = 10

    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images\\mouse.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(240, 600))

    def move_right(self):
        if self.rect.x < 480 - self.rect.h:
            self.rect.x += self.move_speed
        else:
            pass

    def move_left(self):
        if 0 < self.rect.x:
            self.rect.x -= self.move_speed
        else:
            pass
