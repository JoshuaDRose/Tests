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

import pygame
import sprite


class Paddle(sprite.Sprite):
    """ Paddle can hit the ball and move up and down """
    def __init__(self, position: pygame.math.Vector2,
                 group: pygame.sprite.Group):
        super().__init__(position, group)
        self.image = pygame.Surface((20, 100))
        self.rect = self.image.get_rect()
        self.update_collision_box()
        pygame.draw.rect(self.image,
                         (255, 255, 255),
                         self.rect,
                         False,
                         self.rect.width // 2)
        self.direction = pygame.math.Vector2(0, 0)

    def update(self):
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_w]:
            if self.position.y > 0:
                self.direction.y = -1
        if keypress[pygame.K_s]:
            if self.position.y > 800:
                self.direction.y = 1
        self.update_collision_box()
