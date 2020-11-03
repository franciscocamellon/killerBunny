# -*- coding: utf-8 -*-

import pygame

from src.Constants import Game_Constants


class Game_Components(Game_Constants):
    """ Docstring """

    def __init__(self):
        """ Constructor """
        super().__init__()

    def draw_arena(self):
        """ Docstring """
        # self.SCREEN.blit(self.BUNNY, (100, 100))

    def draw_bunny(self):
        """ Docstring """
        self.SCREEN.blit(self.BUNNY, (100, 100))
        for i in range(7):
            for j in range(5):
                self.SCREEN.blit(self.GRASS, (i*100, j*100))
        for y in range(30,350,105):
            self.SCREEN.blit(self.CASTLE,(0,y))

