import pygame
from settings import *

class GameSound:
    def __init__(self):
        self.background_music = 'Background_sound.mp3' # linking to the asset #

    
    def play_background_music(self, loops=-1, volume=0.5): # playing the background music with a loop and reduced volume #
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops)
        return
sounds = GameSound()