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

import unittest
import pygame
from pong import Sprite


class TestSprite(unittest.TestCase):
    """Test sprite baseclass"""

    def setUp(self):
        """Description: Setup constants to be used as test data"""
        self.init()
        self.display = pygame.display.set_mode((800, 800), 0, 32)
        self.empty_group = pygame.sprite.Group()
        self.sprite = Sprite(pygame.math.Vector2(50, 50), self.empty_group)

    def init(self):
        """ Assert all libs are initialized """
        pygame.display.init()
        if not pygame.base.get_init():
            pygame.base.init()
        if not pygame.display.get_init():
            pygame.display.init()
        if pygame.display.get_init():
            self.assertEqual(pygame.display.get_init(), True)
        if pygame.base.get_init():
            self.assertEqual(pygame.base.get_init(), True)

    def assert_between(self, value: int, _min: int, _max: int) -> None:
        """Description: Fail if value is not between min and max (inclusive)"""
        self.assertGreaterEqual(value, _min)
        self.assertLessEqual(value, _max)

    def test_sprite_constructor_size(self):
        """Description: Fail if not in given range"""
        self.assert_between(self.sprite.size, 5, 10)

    def test_update_collision_box(self) -> None:
        """ Test that bounding box applies to position """
        self.sprite.position.x += 5
        self.sprite.position.y += 5
        self.sprite.update_collision_box()
        self.assertEqual(self.sprite.rect.x, round(self.sprite.position.x))
        self.assertEqual(self.sprite.rect.y, round(self.sprite.position.y))

    def test_draw_surface(self) -> None:
        """ Test if surface has been drawn """
        self.sprite.draw(self.display)
