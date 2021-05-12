from data.trash_tube import *


class Trash:
    def __init__(self):

        self._dimX = 200
        self._dimY = 20
        self._weight = 50
        self._height = 50
        self._velocity = 2
        self._color = 255, 0, 0

        self._t_tube = Tube()

        self.TRASH = 5

        # VETRO -----------------------------------------------------------------------
        # Immagine della spazzatura VETRO1
        self.trash_green1 = pygame.image.load('data/assets/images/vetro 1.png')
        self.trash_green_resized1 = pygame.transform.scale(self.trash_green1, (30, 65))

        # Immagine della spazzatura VETRO2
        self.trash_green2 = pygame.image.load('data/assets/images/vetro 2.png')
        self.trash_green_resized2 = pygame.transform.scale(self.trash_green2, (50, 50))

        # Immagine della spazzatura VETRO3
        self.trash_green3 = pygame.image.load('data/assets/images/vetro 3.png')
        self.trash_green_resized3 = pygame.transform.scale(self.trash_green3, (50, 60))

        # Immagine della spazzatura VETRO4
        self.trash_green4 = pygame.image.load('data/assets/images/vetro 4.png')
        self.trash_green_resized4 = pygame.transform.scale(self.trash_green4, (30, 65))

        # CARTA -----------------------------------------------------------------------
        # Immagine della spazzatura CARTA1
        self.trash_yellow1 = pygame.image.load('data/assets/images/cartone 1.png')
        self.trash_yellow_resized1 = pygame.transform.scale(self.trash_yellow1, (40, 65))

        # Immagine della spazzatura CARTA2
        self.trash_yellow2 = pygame.image.load('data/assets/images/cartone 2.png')
        self.trash_yellow_resized2 = pygame.transform.scale(self.trash_yellow2, (50, 60))

        # Immagine della spazzatura CARTA3
        self.trash_yellow3 = pygame.image.load('data/assets/images/cartone 3.png')
        self.trash_yellow_resized3 = pygame.transform.scale(self.trash_yellow3, (60, 50))

        # Immagine della spazzatura CARTA4
        self.trash_yellow4 = pygame.image.load('data/assets/images/cartone 4.png')
        self.trash_yellow_resized4 = pygame.transform.scale(self.trash_yellow4, (40, 65))

        # PLASTICA -----------------------------------------------------------------------
        # Immagine della spazzatura PLASTICA1
        self.trash_blue1 = pygame.image.load('data/assets/images/plastica 1.png')
        self.trash_blue_resized1 = pygame.transform.scale(self.trash_blue1, (30, 65))

        # Immagine della spazzatura PLASTICA2
        self.trash_blue2 = pygame.image.load('data/assets/images/plastica 2.png')
        self.trash_blue_resized2 = pygame.transform.scale(self.trash_blue2, (55, 50))

        # Immagine della spazzatura PLASTICA3
        self.trash_blue3 = pygame.image.load('data/assets/images/plastica 3.png')
        self.trash_blue_resized3 = pygame.transform.scale(self.trash_blue3, (50, 60))

        # Immagine della spazzatura PLASTICA4
        self.trash_blue4 = pygame.image.load('data/assets/images/plastica 4.png')
        self.trash_blue_resized4 = pygame.transform.scale(self.trash_blue4, (50, 55))

        # UMIDO -----------------------------------------------------------------------
        # Immagine della spazzatura UMIDO1
        self.trash_gray1 = pygame.image.load('data/assets/images/cibo 1.png')
        self.trash_gray_resized1 = pygame.transform.scale(self.trash_gray1, (60, 55))

        # Immagine della spazzatura UMIDO2
        self.trash_gray2 = pygame.image.load('data/assets/images/cibo 2.png')
        self.trash_gray_resized2 = pygame.transform.scale(self.trash_gray2, (60, 65))

        # Immagine della spazzatura UMIDO3
        self.trash_gray3 = pygame.image.load('data/assets/images/cibo 3.png')
        self.trash_gray_resized3 = pygame.transform.scale(self.trash_gray3, (60, 55))

        # Immagine della spazzatura UMIDO4
        self.trash_gray4 = pygame.image.load('data/assets/images/cibo 4.png')
        self.trash_gray_resized4 = pygame.transform.scale(self.trash_gray4, (60, 65))

        # Liste di Oggetti da cui random.choiche pesca
        self.color = ['blu', 'grigio', 'verde', 'giallo']
        self.VETRO = [self.trash_green_resized1, self.trash_green_resized2, self.trash_green_resized3,
                      self.trash_green_resized4]
        self.CARTA = [self.trash_yellow_resized1, self.trash_yellow_resized2, self.trash_yellow_resized3,
                      self.trash_yellow_resized4]
        self.PLASTICA = [self.trash_blue_resized1, self.trash_blue_resized2, self.trash_blue_resized3,
                         self.trash_blue_resized4]
        self.UMIDO = [self.trash_gray_resized1, self.trash_gray_resized2, self.trash_gray_resized3,
                      self.trash_gray_resized4]

        # Definizione dello stato Iniziale
        self.state = {
            'x': self._t_tube.randomTube(),
            'y': -1000 - random.randint(0, 1000),
            'image': self.trash_gray_resized4,
            'color': 'grigio',
            'velocity': self.randomVelocity(),
        }
        self.trash_list = [self.state]

        # Inizializzazione della lista con elemanti pari a TRASH
        self.initTrashList()

    def initTrashList(self):

        for i in range(self.TRASH):
            state = {
                'x': self._t_tube.randomTube(),
                'y': -500 - random.randint(0, 1000),
                'color': self.randomColor(),
                'image': self.randomImage(),
                'velocity': self.randomVelocity(),
            }
            self.trash_list.append(state)
        for i in range(self.TRASH):
            for y in range(self.TRASH):
                if self.trash_list[y].get('x') - self.trash_list[i].get('x') < 60:
                    self.trash_list[i].update({'y': -1000 - random.randint(0, 1000)})

    def set_color(self, color):
        self._color = color
        return self._color

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

    def get_velocity(self):
        return self._velocity

    # GESTIONE DELLA SCELTA DEL COLORE E DELL'IMMAGINE RELATIVA AL COLORE e DELLA VELOCITA' -----------------------------
    def randomColor(self):

        random.shuffle(self.color)
        x = random.choice(self.color)
        return x

    def randomImage(self):

        for i in range(len(self.trash_list)):
            if self.trash_list[i].get('color') == 'blu':
                self.trash_list[i].update({'image': self.randomImageBlue()})
            elif self.trash_list[i].get('color') == 'grigio':
                self.trash_list[i].update({'image': self.randomImageGray()})
            elif self.trash_list[i].get('color') == 'verde':
                self.trash_list[i].update({'image': self.randomImageGreen()})
            elif self.trash_list[i].get('color') == 'giallo':
                self.trash_list[i].update({'image': self.randomImageYellow()})

    def randomImageGreen(self):

        random.shuffle(self.VETRO)
        x = random.choice(self.VETRO)
        return x

    def randomImageYellow(self):

        random.shuffle(self.CARTA)
        x = random.choice(self.CARTA)
        return x

    def randomImageBlue(self):

        random.shuffle(self.PLASTICA)
        x = random.choice(self.PLASTICA)
        return x

    def randomImageGray(self):

        random.shuffle(self.UMIDO)
        x = random.choice(self.UMIDO)
        return x

    def randomVelocity(self):

        vel = self.get_velocity() + random.randrange(25, 75, 5) / 100
        return vel

    def chekBorder(self):

        for i in range(self.TRASH):
            if self.trash_list[i].get('y') >= 1200:
                self.trash_list[i].update({'y': -1500 + random.randint(0, 1000)})
                self.trash_list[i].update({'x': self._t_tube.randomTube()})
                if self.trash_list[i].get('y') < 0:
                    if (self.trash_list[i].get('color') == 'blu'):
                        self.trash_list[i].update({'image': self.randomImageBlue()})
                    elif (self.trash_list[i].get('color') == 'grigio'):
                        self.trash_list[i].update({'image': self.randomImageGray()})
                    elif (self.trash_list[i].get('color') == 'verde'):
                        self.trash_list[i].update({'image': self.randomImageGreen()})
                    elif (self.trash_list[i].get('color') == 'giallo'):
                        self.trash_list[i].update({'image': self.randomImageYellow()})

    def updatePosition(self):

        for i in range(self.TRASH):
            vel = self.trash_list[i].get('velocity')
            pos = self.trash_list[i].get('y')
            self.trash_list[i].update({'y': pos + vel})

    def speedUp(self):

        for i in range(self.TRASH):
            currentVelocity = self.trash_list[i].get('velocity')
            self.trash_list[i].update({'velocity': currentVelocity + 0.2})

    # RESET DELLA Y DEGLI OGGETTI DOPO LA PERDITA DI UNA VITA ---------------------------------------------------------

    def resetAfterLifeLoss(self):

        for i in range(self.TRASH):
            self.trash_list[i].update({'y': -1000 + random.randint(0, 1000)})
            self.trash_list[i].update({'x': self._t_tube.randomTube()})
            if self.trash_list[i].get('color') == 'blu':
                self.trash_list[i].update({'image': self.randomImageBlue()})
            elif self.trash_list[i].get('color') == 'grigio':
                self.trash_list[i].update({'image': self.randomImageGray()})
            elif self.trash_list[i].get('color') == 'verde':
                self.trash_list[i].update({'image': self.randomImageGreen()})
            elif self.trash_list[i].get('color') == 'giallo':
                self.trash_list[i].update({'image': self.randomImageYellow()})

    # -----------------------------------------------------------------------------------------------------------------