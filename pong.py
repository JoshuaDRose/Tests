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
import sprite
import pygame


def get_current_directory() -> str:
    """Description: Return the current folder"""
    return os.path.basename(os.path.dirname(os.getcwd()))


if not pygame.display.get_init():
    pygame.display.init()

display = pygame.display.set_mode((800, 800), 0, 32)
sprites = pygame.sprite.Group()
sprite = sprite.Sprite(pygame.math.Vector2(100, 100), sprites)
