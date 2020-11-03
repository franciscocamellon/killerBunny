# -*- coding: utf-8 -*-

import pygame

class Game_Constants():
    """ Docstring """

    def __init__(self):
        """ Constructor """
        self.DISPLAY_NAME = pygame.display.set_caption('Killer Bunny - by Francisco Camello')
        self.FONTSIZE = 20
        self.FONT = pygame.font.Font('freesansbold.ttf', self.FONTSIZE)
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 200
        self.FPSCLOCK = pygame.time.Clock()
        self.BUNNY = pygame.image.load("src/images/dude.png")
        self.GRASS = pygame.image.load("src/images/grass.png")
        self.CASTLE = pygame.image.load("src/images/castle.png")
        self.finish = False
        self.score = 0