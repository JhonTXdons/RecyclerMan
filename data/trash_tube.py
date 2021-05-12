import pygame
import random


class Tube:
    def __init__(self):
        self._dimX = 300
        self._dimY = 0
        self._weight = 300
        self._height = 100

        self.tube = ['tubo1', 'tubo2', 'tubo3']

        # Immagine del Tubo
        self.trash_tube = pygame.image.load('data/assets/images/tubo-1.png')
        self.trash_tube_resized = pygame.transform.scale(self.trash_tube, (300, 100))


    def get_dimX(self):
        return self._dimX

    def get_dimY(self):
        return self._dimY

    def get_weight(self):
        return self._weight

    def get_height(self):
        return self._height

    def randomTube(self):

        random.shuffle(self.tube)
        x = random.choice(self.tube)
        if 'tubo1' in x:
            spawn = random.randint(30, 210)
            return spawn
        if 'tubo2' in x:
            spawn = random.randint(330, 510)
            return spawn
        if 'tubo3' in x:
            spawn = random.randint(630, 810)
            return spawn



