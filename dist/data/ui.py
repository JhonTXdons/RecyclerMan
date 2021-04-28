import pygame

class Ui():
    def __init__(self):
        # Immagine di Bottone Play
        self.b_play = pygame.image.load('data/assets/images/play_button.png')
        self.b_play_resized = pygame.transform.scale(self.b_play, (60, 60))
        self.play_rect = self.b_play_resized.get_rect()
        self.play_rect.x = 970
        self.play_rect.y = 900
        self.b_play_position = self.play_rect.x, self.play_rect.y

        self.play_rect_go = self.b_play_resized.get_rect()
        self.play_rect_go.x = 500
        self.play_rect_go.y = 940
        self.b_play_position_go = self.play_rect_go.x, self.play_rect_go.y

        # Immagine di Bottone Replay
        self.b_replay = pygame.image.load('data/assets/images/replay_button.png')
        self.b_replay_resized = pygame.transform.scale(self.b_replay, (60, 60))
        self.replay_rect = self.b_play_resized.get_rect()
        self.replay_rect.x = 1060
        self.replay_rect.y = 900
        self.b_replay_position = self.replay_rect.x, self.replay_rect.y

        # Immagine di Bottone Pausa
        self.b_pause = pygame.image.load('data/assets/images/pause_button.png')
        self.b_pause_resized = pygame.transform.scale(self.b_pause, (60, 60))
        self.pause_rect = self.b_pause_resized.get_rect()
        self.pause_rect.x = 970
        self.pause_rect.y = 900
        self.b_pause_position = self.pause_rect.x, self.pause_rect.y

        # Immagine di Bottone Esci
        self.b_esc = pygame.image.load('data/assets/images/esc_button.png')
        self.b_esc_resized = pygame.transform.scale(self.b_esc, (60, 60))
        self.esc_rect = self.b_pause_resized.get_rect()
        self.esc_rect.x = 1130
        self.esc_rect.y = 900
        self.b_esc_position = self.esc_rect.x, self.esc_rect.y

        self.esc_rect_go = self.b_play_resized.get_rect()
        self.esc_rect_go.x = 580
        self.esc_rect_go.y = 940
        self.b_esc_position_go = self.esc_rect_go.x, self.esc_rect_go.y

        # Immagine del Cuore pieno
        self.i_heart = pygame.image.load('data/assets/images/cuore.png')
        self.i_heart_resized = pygame.transform.scale(self.i_heart, (40, 40))

        # Immagine del Cuore pieno
        self.i_heart_e = pygame.image.load('data/assets/images/cuore vuoto.png')
        self.i_heart_e_resized = pygame.transform.scale(self.i_heart_e, (40, 40))

