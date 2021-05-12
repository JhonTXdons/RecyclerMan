from data.bin_collector import *
import pygame


class Player:
    def __init__(self):

        self._dimX = 300
        self._dimY = 900
        self._weight = 150
        self._height = 300
        self._velocity = 10
        self._orientation = ''
        self._color = 244, 164, 96

        self.playable_screen = 900

        self._bin = Bin()

    def get_dimX(self):
        return self._dimX

    def get_dimY(self):
        return self._dimY

    def get_weight(self):
        return self._weight

    def get_height(self):
        return self._height

    def get_color(self):
        return self._color

    def pMov(self, KEY):
        if KEY[pygame.K_LEFT] and self._dimX > 0:
            self._dimX -= self._velocity
            self._orientation = 'L'
            return self._orientation

        if KEY[pygame.K_RIGHT] and self._dimX < self.playable_screen - (50 + self._weight):
            self._dimX += self._velocity
            self._orientation = 'R'
            return self._orientation
