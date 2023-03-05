"""
The MIT License (MIT)

Copyright (c) 2023 Author

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""

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
        self._alpha = 255
        self._visible = self.alpha != 0
        self.visible = True

    def update_collision_box(self) -> None:
        """Update collision box"""
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)

    def draw(self, surface: pygame.surface.Surface):
        """ Draw sprite to surface """
        self.image.set_alpha(self.alpha)
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self) -> None:
        """ Call update functions individually """
        self.update_collision_box()

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = value

    @alpha.deleter
    def alpha(self):
        del self._alpha

    @property
    def visible(self):
        return self._visible

    @visible.getter
    def visible(self):
        return self._visible > 0

    @visible.setter
    def visible(self, value):
        self._visible = value

    @visible.deleter
    def visible(self):
        del self._visible
