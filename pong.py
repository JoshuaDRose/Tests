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

import os
from random import randint

import pygame


def get_current_directory() -> str:
    """Description: Return the current folder"""
    return os.path.basename(os.path.dirname(os.getcwd()))


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


if not pygame.display.get_init():
    pygame.display.init()

display = pygame.display.set_mode((800, 800), 0, 32)
sprites = pygame.sprite.Group()
sprite = Sprite(pygame.math.Vector2(100, 100), sprites)
