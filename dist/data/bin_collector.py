import pygame

class Bin():
    def __init__(self):
        self._dimX = 400
        self._dimY = 950
        self._weight = 100
        self._height = 100
        self._velocity = 10
        self._orientation = True


        # BIDONI -----------------------------------------------------------------------
        # Immagine del bidone BLU
        self.bin_blue = pygame.image.load('data/assets/images/bidone blu.png')
        self.bin_blue_resized = pygame.transform.scale(self.bin_blue, (100, 100))
        self._type = self.bin_blue_resized
        # Immagine del bidone VERDE
        self.bin_green = pygame.image.load('data/assets/images/bidone verde.png')
        self.bin_green_resized = pygame.transform.scale(self.bin_green, (100, 100))
        # Immagine del bidone GRIGIO
        self.bin_gray = pygame.image.load('data/assets/images/bidone grigio.png')
        self.bin_gray_resized = pygame.transform.scale(self.bin_gray, (100, 100))
        # Immagine del bidone GIALLO
        self.bin_yellow = pygame.image.load('data/assets/images/bidone giallo.png')
        self.bin_yellow_resized = pygame.transform.scale(self.bin_yellow, (100, 100))



    def set_dimX(self, dimX):
        self._dimX = dimX
        print(self._dimX)
        return  self._dimX

    def set_color(self, color):
        self._color = color
        return self._color

    def set_type(self, type):
        self._type = type
        return self._type

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

    def get_type(self):
        return self._type

    def bMov(self, KEY):
        if KEY[pygame.K_LEFT] and self._dimX > self._weight + self._velocity:
            self._dimX -= self._velocity
            self._orientation = True
            return self._orientation
        if KEY[pygame.K_RIGHT] and self._dimX < 900 - self._weight:
            self._dimX += self._velocity
            self._orientation = False
            return self._orientation

