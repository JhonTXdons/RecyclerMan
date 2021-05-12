import pygame.rect

from data.trash import *
from data.player import *
from data.ui import *


class App:

    def __init__(self):
        self._running = True

        # GAME STATES -------------------------------------------------------------------------------------------------
        self.menu = True
        self.PLAY_STATE = False
        self.PAUSE_STATE = False
        self.LOST_STATE = False
        self.WIN_STATE = False
        # -------------------------------------------------------------------------------------------------------------

        # MAIN SCREEN DEFINITION --------------------------------------------------------------------------------------
        self._display_surf = None
        self.clock = pygame.time.Clock()
        self._title_ = None

        self._p = Player()
        self._bin = Bin()
        self._t_tube = Tube()
        self._t = Trash()
        self._ui = Ui()

        pygame.font.init()
        self.font = pygame.font.Font('data/assets/fonts/Coiny-Regular.ttf', 20)

        # Numero di spazzatura da iterare
        self.TRASH = self._t.TRASH
        self.trash_list = self._t.trash_list

        # Proprietà dello Schermo
        self.size = self.weight, self.height = 1200, 1200
        self._display_surf = pygame.display.set_mode(self.size)
        self._title_ = pygame.display.set_caption("Recycler Man")

        # PUNTEGGIO
        self.POINT = 0
        self.BEST_POINT = 0
        self.point_check = 0
        self.point_text1 = self.font.render("PUNTEGGIO", True, (0, 0, 0))
        self.point_text2 = self.font.render(str(self.POINT), True, (0, 0, 0))

        # INQUINAMENTO
        self.POLLUTION = 0
        self.gm_pollution = False
        self.pollution_text1 = self.font.render("INQUINAMENTO", True, (255, 0, 0))
        self.pollution_text2 = self.font.render(str(self.POLLUTION) + " %", True, (255, 0, 0))

        # VITA
        self.VITA = 3
        self.life_text1 = self.font.render("VITE", True, (255, 0, 0))
        self.life_text2 = self.font.render(str(self.VITA), True, (255, 0, 0))

        # Immagine di Menu
        self.mn = pygame.image.load('data/assets/images/home.png')
        self.mn_resized = pygame.transform.scale(self.mn, (1200, 1200))
        self.mn_resized_HD = pygame.transform.scale(self.mn, (1000, 1000))

        # Immagine di Background
        self.bg = pygame.image.load('data/assets/images/sfondo.png').convert()
        self.bg_resized = pygame.transform.scale(self.bg, (900, 1200))

        # Immagine di Background_Muro
        self.bg_w = pygame.image.load('data/assets/images/muro.png').convert()
        self.bg_w_resized = pygame.transform.scale(self.bg_w, (300, 1200))

        # Immagine di Background_Muro_Tasti
        self.bg_w_keys = pygame.image.load('data/assets/images/pulsanti-wasd.png')

        # Immagine del giocatore
        self.player = pygame.image.load('data/assets/images/omino.png')
        self.L_payer_resized = pygame.transform.scale(self.player, (150, 300))

    def on_init(self):
        pygame.init()
        self.PLAY_STATE = True

    # GESTIONE DELLE PROPRIETA' DEL GIOCATORE, BIDONE e TUBO ----------------------------------------------------------

    def getPlayerStat(self):
        PlayerX = self._p.get_dimX()
        PlayerY = self._p.get_dimY()
        PlayerWeight = self._p.get_weight()
        PlayerHeight = self._p.get_height()
        PlayerPosition = PlayerX, PlayerY, PlayerWeight, PlayerHeight
        return PlayerPosition

    def getScoreLifePollution(self, score, life, pollution):

        self.point_text2 = self.font.render(str(score), True, (0, 0, 0))

        if self.gm_pollution:
            self.pollution_text2 = self.font.render(str(pollution) + " %", True, (255, 0, 0))
            if life == 3:
                self._display_surf.blit(self._ui.i_heart_resized, [970, 400])
                self._display_surf.blit(self._ui.i_heart_resized, [1020, 400])
                self._display_surf.blit(self._ui.i_heart_resized, [1070, 400])
            elif life == 2:
                self._display_surf.blit(self._ui.i_heart_e_resized, [970, 400])
                self._display_surf.blit(self._ui.i_heart_resized, [1020, 400])
                self._display_surf.blit(self._ui.i_heart_resized, [1070, 400])
            elif life == 1:
                self._display_surf.blit(self._ui.i_heart_e_resized, [970, 400])
                self._display_surf.blit(self._ui.i_heart_e_resized, [1020, 400])
                self._display_surf.blit(self._ui.i_heart_resized, [1070, 400])
            elif life == 0:
                self._display_surf.blit(self._ui.i_heart_e_resized, [970, 400])
                self._display_surf.blit(self._ui.i_heart_e_resized, [1020, 400])
                self._display_surf.blit(self._ui.i_heart_e_resized, [1070, 400])
                self.LOST_STATE = True
                self.PLAY_STATE = False
        else:
            if life == 3:
                self._display_surf.blit(self._ui.i_heart_resized, [970, 360])
                self._display_surf.blit(self._ui.i_heart_resized, [1020, 360])
                self._display_surf.blit(self._ui.i_heart_resized, [1070, 360])
            elif life == 2:
                self._display_surf.blit(self._ui.i_heart_e_resized, [970, 360])
                self._display_surf.blit(self._ui.i_heart_resized, [1020, 360])
                self._display_surf.blit(self._ui.i_heart_resized, [1070, 360])
            elif life == 1:
                self._display_surf.blit(self._ui.i_heart_e_resized, [970, 360])
                self._display_surf.blit(self._ui.i_heart_e_resized, [1020, 360])
                self._display_surf.blit(self._ui.i_heart_resized, [1070, 360])
            elif life == 0:
                self._display_surf.blit(self._ui.i_heart_e_resized, [970, 360])
                self._display_surf.blit(self._ui.i_heart_e_resized, [1020, 360])
                self._display_surf.blit(self._ui.i_heart_e_resized, [1070, 360])
                self.LOST_STATE = True
                self.PLAY_STATE = False

    def getBinStat(self):
        BinX = self._bin.get_dimX()
        BinY = self._bin.get_dimY()
        BinWeight = self._bin.get_weight()
        BinHeight = self._bin.get_height()
        BinPosition = BinX, BinY, BinWeight, BinHeight
        return BinPosition

    def getTubeStat(self):
        TubeX = self._t_tube.get_dimX()
        TubeY = self._t_tube.get_dimY()
        TubeWeight = self._t_tube.get_weight()
        TubeHeight = self._t_tube.get_height()
        TubePosition = TubeX, TubeY, TubeWeight, TubeHeight
        return TubePosition

    # -----------------------------------------------------------------------------------------------------------------

    def playerBinLoop(self):

        keys = pygame.key.get_pressed()

        self._bin.bMov(keys)
        self._display_surf.blit(self._bin.get_type(), self.getBinStat())
        self._bin.binChangeColor(keys)

        self._p.pMov(keys)
        self._display_surf.blit(pygame.transform.flip(self.player, True, False), self.getPlayerStat())

    def trashLoop(self):

        for i in range(self.TRASH):
            self._display_surf.blit(self.trash_list[i].get('image'),
                                    (self.trash_list[i].get('x'), self.trash_list[i].get('y')))

        self._display_surf.blit(self._t_tube.trash_tube_resized, self.getTubeStat())
        self._display_surf.blit(self._t_tube.trash_tube_resized, (0, 0, 300, 100))
        self._display_surf.blit(self._t_tube.trash_tube_resized, (600, 0, 300, 100))

        self._t.updatePosition()
        self.checkCollisionBin()
        self.mode_pollution(self.gm_pollution)
        self._t.chekBorder()

        # Aumento di velocità in base al punteggio raggiunto ----------------------------------------------------------
        if 500 <= self.POINT < 2500 and self.point_check == 0:
            self._t.speedUp()
            self.point_check = 1  # impedisce che speedUp venga chiamata in continuazione
        if 2500 <= self.POINT < 5000 and self.point_check == 1:
            self._t.speedUp()
            self.point_check = 2
        if 5000 <= self.POINT < 7500 and self.point_check == 2:
            self._t.speedUp()
            self.point_check = 3

    # -----------------------------------------------------------------------------------------------------------------
    # CONTROLLO COLLISIONI CON IL BIDONE ------------------------------------------------------------------------------

    def checkCollisionBin(self):

        for i in range(self.TRASH):
            rec1 = self._bin.bin_blue_resized.get_rect()
            rec1.x = self._bin.get_dimX()
            rec1.y = self._bin.get_dimY()

            rec2 = self.trash_list[i].get('image').get_rect()
            rec2.x = self.trash_list[i].get('x')
            rec2.y = self.trash_list[i].get('y')

            if rec2.colliderect(rec1) and self.VITA != 0:
                if self._bin.get_color() == self.trash_list[i].get('color'):
                    self.POINT += 100
                    self.trash_list[i].update({'y': -1500 + random.randint(0, 1000)})
                    self.trash_list[i].update({'x': self._t_tube.randomTube()})
                    if self.trash_list[i].get('color') == 'blu':
                        self.trash_list[i].update({'image': self._t.randomImageBlue()})
                    elif self.trash_list[i].get('color') == 'grigio':
                        self.trash_list[i].update({'image': self._t.randomImageGray()})
                    elif self.trash_list[i].get('color') == 'verde':
                        self.trash_list[i].update({'image': self._t.randomImageGreen()})
                    elif self.trash_list[i].get('color') == 'giallo':
                        self.trash_list[i].update({'image': self._t.randomImageYellow()})
                    print(self.POINT)
                else:
                    self.VITA -= 1
                    self._t.resetAfterLifeLoss()
            else:
                pass

    # -----------------------------------------------------------------------------------------------------------------

    def main_loop(self):

        if self.on_init() == False:
            self._running = False

        while self._running:
            if self.menu:
                self.main_menu()
            elif self.PLAY_STATE:
                self.game_play()
            elif self.LOST_STATE and self.VITA == 0:
                self.game_over()
            elif self.WIN_STATE:
                self.game_win()
        self.on_cleanup()

    def on_cleanup(self):
        pygame.quit()

    # GAME ----------------------------------------------------------------------------------------------------------

    def main_menu(self):

        self._display_surf.fill((255, 255, 255))
        self._display_surf.blit(self.mn_resized, [0, 0])

        title_text = pygame.image.load('data/assets/images/titolo.png')
        title_resized = pygame.transform.scale(title_text, (500, 200))

        font = pygame.font.Font('data/assets/fonts/ARCADECLASSIC.TTF', 30)
        play_text = font.render("GIOCA", True, (255, 255, 255))
        self._display_surf.blit(title_resized, [380, 530])
        self._display_surf.blit(play_text, [590, 800])

        rect = pygame.Rect(470, 775, 330, 90)

        while self.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False
                    self._running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and rect.collidepoint(pos):
                        self.game_mode_switch()
            pygame.display.flip()
            self.clock.tick(60)

    def game_mode_switch(self):

        reading = True
        self._display_surf.fill((0, 0, 0))
        font = pygame.font.Font('data/assets/fonts/Coiny-Regular.ttf', 35)
        text1 = font.render("SCEGLI LA MODALITA' GIOCO", True, (255, 255, 255))
        text2 = font.render("INFINITA", True, (255, 255, 255))
        text3 = font.render("INQUINAMENTO", True, (255, 255, 255))
        self._display_surf.blit(text1, [300, 150])
        self._display_surf.blit(text2, [450, 300])
        self._display_surf.blit(text3, [450, 400])

        R_rect = text2.get_rect()
        R_rect.x = 450
        R_rect.y = 300

        L_rect = text3.get_rect()
        L_rect.x = 450
        L_rect.y = 400

        while reading:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    reading = False
                    self.menu = False
                    self._running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and R_rect.collidepoint(pos):
                        reading = False
                        self.tutorial_infinite()
                    if pygame.mouse.get_pressed()[0] and L_rect.collidepoint(pos):
                        reading = False
                        self.tutorial_pollution()
            pygame.display.flip()
            self.clock.tick(60)

    def tutorial_infinite(self):

        reading = True
        self._display_surf.fill((255, 255, 255))

        tut_image = pygame.image.load('data/assets/images/tutorial3.png')
        tut_image_resized = pygame.transform.scale(tut_image, (1200, 1200))
        self._display_surf.blit(tut_image_resized, [0, 0])

        left_arrow = pygame.image.load('data/assets/images/left_arrow.png')
        left_arrow_resized = pygame.transform.scale(left_arrow, (200, 100))
        right_arrow_resized = pygame.transform.flip(left_arrow_resized, True, False)
        self._display_surf.blit(left_arrow_resized, [150, 1050])
        self._display_surf.blit(right_arrow_resized, [900, 1050])

        R_rect = right_arrow_resized.get_rect()
        R_rect.x = 900
        R_rect.y = 1050

        L_rect = left_arrow_resized.get_rect()
        L_rect.x = 150
        L_rect.y = 1050

        while reading:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    reading = False
                    self.menu = False
                    self._running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and R_rect.collidepoint(pos):
                        self.menu = False
                        reading = False
                        self.gm_pollution = False
                        self.PLAY_STATE = True
                    if pygame.mouse.get_pressed()[0] and L_rect.collidepoint(pos):
                        reading = False
                        self.game_mode_switch()
            pygame.display.flip()
            self.clock.tick(60)

    def tutorial_pollution(self):

        reading = True
        self._display_surf.fill((255, 255, 255))

        tut_image = pygame.image.load('data/assets/images/tutorial2.png')
        tut_image_resized = pygame.transform.scale(tut_image, (1200, 1200))
        self._display_surf.blit(tut_image_resized, [0, 0])

        left_arrow = pygame.image.load('data/assets/images/left_arrow.png')
        left_arrow_resized = pygame.transform.scale(left_arrow, (200, 100))
        right_arrow_resized = pygame.transform.flip(left_arrow_resized, True, False)
        self._display_surf.blit(left_arrow_resized, [150, 1050])
        self._display_surf.blit(right_arrow_resized, [900, 1050])

        R_rect = right_arrow_resized.get_rect()
        R_rect.x = 900
        R_rect.y = 1050

        L_rect = left_arrow_resized.get_rect()
        L_rect.x = 150
        L_rect.y = 1050

        while reading:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    reading = False
                    self.menu = False
                    self._running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and R_rect.collidepoint(pos):
                        reading = False
                        self.menu = False
                        self.PLAY_STATE = True
                        self.gm_pollution = True
                    if pygame.mouse.get_pressed()[0] and L_rect.collidepoint(pos):
                        reading = False
                        self.game_mode_switch()
            pygame.display.flip()
            self.clock.tick(60)

    # GAME STATES -----------------------------------------------------------------------------------------------------
    def game_play(self):

        while self.PLAY_STATE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.PLAY_STATE = False
                    self._running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.PAUSE_STATE = not self.PAUSE_STATE
                    if event.key == pygame.K_r:
                        self.game_replay()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and self._ui.pause_rect.collidepoint(pos):
                        self.PAUSE_STATE = not self.PAUSE_STATE
                    if pygame.mouse.get_pressed()[0] and self._ui.replay_rect.collidepoint(pos):
                        self.game_replay()
                    if pygame.mouse.get_pressed()[0] and self._ui.esc_rect.collidepoint(pos):
                        self.menu = True
                        self.VITA = 3
                        self.POINT = 0
                        self._t.resetAfterLifeLoss()
                        self.LOST_STATE = False
                        self.PLAY_STATE = False

            self._display_surf.fill((0, 0, 0))
            self._display_surf.blit(self.bg_resized, [0, 0])
            self._display_surf.blit(self.bg_w_resized, [900, 0])

            if self.gm_pollution:
                self._display_surf.blit(self.point_text1, [970, 250])
                self._display_surf.blit(self.point_text2, [970, 280])
                self._display_surf.blit(self.pollution_text1, [970, 310])
                self._display_surf.blit(self.pollution_text2, [970, 340])
                self._display_surf.blit(self.life_text1, [970, 370])
            else:
                self._display_surf.blit(self.point_text1, [970, 250])
                self._display_surf.blit(self.point_text2, [970, 280])
                self._display_surf.blit(self.life_text1, [970, 320])

            self.playerBinLoop()
            self.trashLoop()
            self.getScoreLifePollution(self.POINT, self.VITA, self.POLLUTION)

            # UI -------------------------------------------------------------
            self._display_surf.blit(self.bg_w_keys, [950, 600])
            if self.PAUSE_STATE:
                self.game_pause()
            else:
                self._display_surf.blit(self._ui.b_pause_resized, [950, 900])
                self._display_surf.blit(self._ui.b_replay_resized, [1030, 900])
                self._display_surf.blit(self._ui.b_esc_resized, [1110, 900])

            pygame.display.flip()
            self.clock.tick(60)

    def game_replay(self):

        self.VITA = 3
        self.BEST_POINT = self.POINT
        self.POINT = 0
        self.LOST_STATE = False
        self.WIN_STATE = False
        self.PLAY_STATE = True
        self._t.initTrashList()

    def game_pause(self):

        self._display_surf.blit(self._ui.b_play_resized, [950, 900])
        self._display_surf.blit(self._ui.b_replay_resized, [1030, 900])
        self._display_surf.blit(self._ui.b_esc_resized, [1110, 900])

        while self.PAUSE_STATE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.PAUSE_STATE = not self.PAUSE_STATE
                    self.PLAY_STATE = False
                    self.menu = False
                    self._running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and self._ui.play_rect.collidepoint(pos):
                        self.PAUSE_STATE = not self.PAUSE_STATE
                    if pygame.mouse.get_pressed()[0] and self._ui.replay_rect.collidepoint(pos):
                        self.PAUSE_STATE = not self.PAUSE_STATE
                        self.game_replay()
                    if pygame.mouse.get_pressed()[0] and self._ui.esc_rect.collidepoint(pos):
                        self.PAUSE_STATE = not self.PAUSE_STATE
                        self.PLAY_STATE = False
                        self.menu = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.PAUSE_STATE = not self.PAUSE_STATE
                    if event.key == pygame.K_p:
                        self.PAUSE_STATE = not self.PAUSE_STATE
                    if event.key == pygame.K_r:
                        self.PAUSE_STATE = not self.PAUSE_STATE
                        self.game_replay()
            pygame.display.update()
            self.clock.tick(60)

    def game_win(self):

        # Immagine di Background
        bg_loss = pygame.image.load('data/assets/images/sfondo_win.png')
        bg_loss_resized = pygame.transform.scale(bg_loss, (1200, 1200))
        self._display_surf.blit(bg_loss_resized, [0, 0])

        font = pygame.font.Font('data/assets/fonts/ARCADECLASSIC.TTF', 60)
        font2 = pygame.font.Font('data/assets/fonts/ARCADECLASSIC.TTF', 35)
        game_over_text = font.render("VITTORIA", True, (255, 0, 0))
        point_text3 = font2.render("PUNTEGGIO", True, (0, 0, 0))
        point_text4 = font2.render(str(self.POINT), True, (0, 0, 0))
        self._display_surf.blit(game_over_text, [450, 520])
        self._display_surf.blit(point_text3, [500, 620])
        self._display_surf.blit(point_text4, [550, 650])

        # UI --------------------------------------------------------------------------------------------------------
        self._display_surf.blit(self._ui.b_play_resized, [500, 940])
        self._display_surf.blit(self._ui.b_esc_resized, [580, 940])
        # -----------------------------------------------------------------------------------------------------------

        while self.WIN_STATE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.WIN_STATE = False
                    self._running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and self._ui.play_rect_go.collidepoint(pos):
                        self.game_replay()
                    if pygame.mouse.get_pressed()[0] and self._ui.esc_rect_go.collidepoint(pos):
                        self.WIN_STATE = not self.WIN_STATE
                        self.menu = not self.menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.WIN_STATE = False
                        self.menu = True
                    if event.key == pygame.K_p:
                        self.WIN_STATE = False
                        self.PLAY_STATE = True
            pygame.display.update()
            self.clock.tick(60)

    def game_over(self):

        # Immagine di Background
        bg_loss = pygame.image.load('data/assets/images/sfondo_lost.png')
        bg_loss_resized = pygame.transform.scale(bg_loss, (1200, 1200))
        self._display_surf.blit(bg_loss_resized, [0, 0])

        font = pygame.font.Font('data/assets/fonts/ARCADECLASSIC.TTF', 60)
        font2 = pygame.font.Font('data/assets/fonts/ARCADECLASSIC.TTF', 35)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        point_text3 = font2.render("PUNTEGGIO", True, (0, 0, 0))
        point_text4 = font2.render(str(self.POINT), True, (0, 0, 0))
        self._display_surf.blit(game_over_text, [450, 520])
        self._display_surf.blit(point_text3, [500, 620])
        self._display_surf.blit(point_text4, [550, 650])

        # UI --------------------------------------------------------------------------------------------------------
        self._display_surf.blit(self._ui.b_play_resized, [500, 940])
        self._display_surf.blit(self._ui.b_esc_resized, [580, 940])
        # -----------------------------------------------------------------------------------------------------------

        while self.LOST_STATE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.LOST_STATE = False
                    self._running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and self._ui.play_rect_go.collidepoint(pos):
                        self.game_replay()
                    if pygame.mouse.get_pressed()[0] and self._ui.esc_rect_go.collidepoint(pos):
                        self.LOST_STATE = not self.LOST_STATE
                        self.menu = not self.menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.LOST_STATE = False
                        self.menu = True
                    if event.key == pygame.K_p:
                        self.LOST_STATE = False
                        self.PLAY_STATE = True
            pygame.display.update()
            self.clock.tick(60)

    # GAME MODE POLLUTION ---------------------------------------------------------------------------------------------
    def mode_pollution(self, gm):

        if gm == True:
            for i in range(self.TRASH):
                if self.trash_list[i].get('y') >= 1200:
                    self.POLLUTION += 5
                    print(str(self.POLLUTION))
        if self.POINT == 10000 and self.POLLUTION != 100:
            self.WIN_STATE = True
            self.PLAY_STATE = False
        if self.POLLUTION == 100:
            self.LOST_STATE = True
            self.PLAY_STATE = False


if __name__ == "__main__":
    theApp = App()
    theApp.main_loop()
