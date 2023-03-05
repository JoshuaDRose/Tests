from random import randint
import pygame


class Sprite(pygame.sprite.Sprite):
    """Baseclass for sprites and entities"""

    def __init__(self,
                 position: pygame.math.Vector2,
                 group: pygame.sprite.Group):
        """Description: Constructor for baseclass
        position: position of sprite (x, y)
        group: requires pygame.sprite.Group
        """
        super().__init__(group)
        self.size = randint(5, 10)
        self.position = position
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)

    def update_collision_box(self) -> None:
        """Update collision box"""
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)

    def draw(self, surface: pygame.surface.Surface):
        """ Draw sprite to surface """
        surface.blit(self.image, (self.rect.x, self.rect.y))
