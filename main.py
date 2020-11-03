# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *
import math

# from src.Constants import Game_Constants as const
# from src.Components import Game_Components as components


class Killer_Bunny():
    """ Docstring """

    def __init__(self):
        """ Constructor """

        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Killer Bunny - by Francisco Camello')
        self.FONTSIZE = 20
        self.FONT = pygame.font.Font('freesansbold.ttf', self.FONTSIZE)
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 200
        self.FPSCLOCK = pygame.time.Clock()
        self.BUNNY = ''
        self.GRASS = ''
        self.CASTLE = ''
        self.ARROW = ''
        self.BLACK_COLOR = (0,0,0)
        self.WHITE_COLOR = (255,255,255)
        self.finish = False
        self.keys = [False, False, False, False]
        self.bunny = ''
        self.bunny_position = [100,100]
        self.mouse_pos = [0,0]
        self.click_pos = [0,0]
        self.arrows = []
        self.score = 0

    def load_images(self):
        self.BUNNY = pygame.image.load("src/images/dude.png")
        self.GRASS = pygame.image.load("src/images/grass.png")
        self.CASTLE = pygame.image.load("src/images/castle.png")
        self.ARROW = pygame.image.load("src/images/bullet.png")

    def draw_arena(self):
        self.load_images()

        X_range = self.SCREEN_WIDTH // self.GRASS.get_width() + 1
        y_range = self.SCREEN_HEIGHT // self.GRASS.get_height() + 1

        for i in range(X_range):
            for j in range(y_range):
                self.SCREEN.blit(self.GRASS, (i*100, j*100))

        for y in range(30,350,105):
            self.SCREEN.blit(self.CASTLE,(0,y))

    def draw_bunny(self, position):
        self.SCREEN.blit(self.BUNNY, (position[0],position[1]))

    def move_bunny(self, key, position):
        if key[0] and position[1] > 0:
            position[1] -= 5
        elif key[2] and position[1] < 420:
            position[1] += 5
        if key[1] and position[0] > 0:
            position[0] -= 5
        elif key[3] and position[0] < 570:
            position[0] += 5
        return position

    def spin_bunny(self, mouse_pos, bunny_pos):

        x,y = (mouse_pos[1]-(bunny_pos[1]), mouse_pos[0]-(bunny_pos[0]))
        rad_degrees = math.atan2(x,y)
        degree = math.degrees(rad_degrees)
        self.BUNNY = pygame.transform.rotozoom(self.BUNNY, -degree, 1)

    def draw_arrows(self, arrows):
        for arrow in arrows:
            i = 0
            x_velocity = math.cos(arrow[0]) * 10
            y_velocity = math.sin(arrow[0]) * 10
            arrow[1] += x_velocity
            arrow[2] += y_velocity
            if arrow[1] < -64 or arrow[1] > 640 or arrow[2] < -64 or arrow[2] > 480:
                arrows.pop(i)
            i += 1
            for _arrow in arrows:
                temp_arrow = pygame.transform.rotate(self.ARROW, 360 - _arrow[0] * 57.29)
                self.SCREEN.blit(temp_arrow, (_arrow[1], _arrow[2]))



    def init_game(self):
        """ Docstring """


        while not self.finish:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.finish = True

                if event.type == pygame.KEYDOWN:
                    if event.key == K_w:
                        self.keys[0] = True
                    elif event.key == K_a:
                        self.keys[1] = True
                    elif event.key == K_s:
                        self.keys[2] = True
                    elif event.key == K_d:
                        self.keys[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == K_w:
                        self.keys[0] = False
                    elif event.key == K_a:
                        self.keys[1] = False
                    elif event.key == K_s:
                        self.keys[2] = False
                    elif event.key == K_d:
                        self.keys[3] = False

                if event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_pos = pygame.mouse.get_pos()
                    self.arrows.append([math.atan2(self.click_pos[1] - (self.bunny_position[1] + 32), self.click_pos[0] - (self.bunny_position[0] + 32)), self.click_pos[0] + 32, self.bunny_position[1] + 32])


            self.draw_arena()
            self.bunny_position = self.move_bunny(self.keys, self.bunny_position)
            print(self.arrows)
            # print('mouse_pos[1]: ',self.mouse_pos[1])
            self.spin_bunny(self.mouse_pos, self.bunny_position)
            self.draw_bunny(self.bunny_position)
            self.draw_arrows(self.arrows)


            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()

        pygame.quit()
        sys.exit()


Killer_Bunny().init_game()
