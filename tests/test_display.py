#!/usr/bin/env python3
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import time
import unittest
import microstacknode.hardware.display.ssd1306
from microstacknode.hardware.display.font import (FourByFiveFont,
                                                  MinecraftiaFont)
from microstacknode.hardware.display.sprite import (Sprite,
                                                    CharSprite,
                                                    StringSprite)


class TestMMA8452Q(unittest.TestCase):

    def setUp(self):
        self.display = microstacknode.hardware.display.ssd1306.SSD1306()
        self.display.init()

    @unittest.skip
    def test_character_printing(self):
        char_sprite = CharSprite('a', FourByFiveFont())
        self.display.draw_sprite(0, 0, char_sprite)

    def test_character_printing(self):
        str_sprite = StringSprite('ALPHABET', 'R', MinecraftiaFont())
        self.display.draw_sprite(0, 0, str_sprite)

    def test_rectangle(self):
        sprite = Sprite(96,16)
        sprite.draw_rectangle(2,3,4,5,1)
        sprite.draw_rectangle(30,3,5,5)     
        self.display.draw_sprite(0,0, sprite)


if __name__ == "__main__":
    unittest.main()
