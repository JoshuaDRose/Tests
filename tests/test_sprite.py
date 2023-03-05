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
import sprite


class TestSprite(unittest.TestCase):
    """Test sprite baseclass"""

    def setUp(self):
        """Description: Setup constants to be used as test data"""
        self.display = pygame.display.set_mode((800, 800), 0, 32)
        self.empty_group = pygame.sprite.Group()
        self.sprite = sprite.Sprite(
                pygame.math.Vector2(50, 50),
                self.empty_group)

    def assert_between(self, value: int, _min: int, _max: int) -> None:
        """Description: Fail if value is not between min and max (inclusive)"""
        self.assertGreaterEqual(value, _min)
        self.assertLessEqual(value, _max)

    def test_assert_between(self):
        x = 2
        y = 10
        z = 5
        self.assert_between(z, x, y)

    def test_sprite_constructor_size(self):
        """Description: Fail if not in given range"""
        assert (self.sprite.size in range(5, 11)) == True

    def test_update_collision_box(self) -> None:
        """ Test that bounding box applies to position """
        self.sprite.position.x += 5
        self.sprite.position.y += 5
        self.sprite.update_collision_box()
        assert self.sprite.rect.x == round(self.sprite.position.x)
        assert self.sprite.rect.y == round(self.sprite.position.y)

    def test_draw_surface(self) -> None:
        """ Test if surface has been drawn """
        self.sprite.draw(self.display)

    def test_draw_set_alpha(self):
        """ Test alpha is applied to surface on draw """
        self.sprite.alpha = 128
        self.sprite.draw(self.display)
        assert self.sprite.image.get_alpha() == self.sprite.alpha

    def test_update_method(self):
        """ Test each function has been called individually """
        self.sprite.update()
        self.test_update_collision_box()
