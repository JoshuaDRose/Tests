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

import sys
import os
import paddle
import pygame


def get_current_directory() -> str:
    """Description: Return the current folder"""
    return os.path.basename(os.path.dirname(os.getcwd()))


if not pygame.display.get_init():
    pygame.display.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((800, 800), 0, 32)
paddles = pygame.sprite.Group()
paddle = paddle.Paddle(pygame.math.Vector2(0, 0), paddles)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill((0, 0, 0))

    for paddle in paddles:
        if paddle.direction.y:
            paddle.position.y += 1
        elif paddle.direction.y:
            paddle.position.y -= 1
        paddle.draw(display)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
