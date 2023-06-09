import random
import pygame
from game_settings import settings


class Food(pygame.sprite.Sprite):
    """
    Food sprite. This class setting move, fall, rotation, etc
    """

    def __init__(self, surface, group):
        """
        Create cheese entity and adding it to food group
        :param surface:
        :param group:
        """

        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load('images/cheese.bmp')
        self.image = self.original_image.copy
        self.original_image.set_colorkey((255, 255, 255))

        # Cheese spawn parameters
        self.rect = self.original_image.get_rect(
            center=(
                # Spawning horizontal coordinates
                random.randint(
                    27,
                    surface.get_width() - 27
                ),
                -15  # Spawning altitude
            )
        )

        self.fall_speed = settings.food_speed
        self.rotate = 0
        self.rotation_speed = 2
        self.add(group)

    def update(self, surface):
        """
        Set rotation and falling food

        :param surface:
        :return: False if game quit
        """

        self.rotate = (self.rotate + self.rotation_speed) % 360
        rotated_image = pygame.transform.rotate(self.original_image, self.rotate)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        self.image = rotated_image
        self.rect = rotated_rect
        surface.blit(rotated_image, rotated_rect)

        if self.rect.y < 640:
            self.rect.y += self.fall_speed
        else:
            settings.game_active = False

    def catch(self):
        """
        Delete food if player catch it
        :return:
        """
        self.kill()
