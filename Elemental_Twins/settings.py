import pygame 
# Determining the screen width and height for the game window #
SCREEN_WIDTH = 1008
SCREEN_HEIGHT = 672

# game options/settings
TITLE = "Elemental Twins" # Determining the TITLE which will be shown on the menu screen # 
FPS = 60 # Setting Frames Per Second for the game #
TILE_SIZE = 24 # Setting each tile size for the game #

PLAYER1_KEYS = {"right": pygame.K_d, "left": pygame.K_a, "up": pygame.K_w} # Red Player movements are w, a, s and d #
PLAYER2_KEYS = {"right": pygame.K_RIGHT, "left": pygame.K_LEFT, "up": pygame.K_UP} # Blue Player movements are up, right, left and bottom arrows # 

# map info each letter represents an element on the game screen #
MAP_WALL = '1'
MAP_PLAYER1 = 'p'
MAP_PLAYER2 = 'P'
MAP_LAVA = 'l'
MAP_WATER = 'w'
MAP_LAVA_GEM = 'L'
MAP_WATER_GEM = 'W'
MAP_LAVA_DOOR = 'd'
MAP_WATER_DOOR = 'D'
MAP_GUN_RIGHT = 'g'
MAP_GUN_LEFT = 'G'
MAP_FIRE_GUN_RIGHT = 'f'
MAP_FIRE_GUN_LEFT = 'F'
MAP_WATER_GUN_RIGHT = 'b'
MAP_WATER_GUN_LEFT = 'B'

# colors identified using RGB tuples #
WHITE = (222, 222, 222)
BLACK = (22, 22, 22)
GREY = (100, 100, 100)
RED = (174, 0, 0)
GREEN = (40, 222, 20)
BLUE = (59, 166, 255)
YELLOW = (255, 255 ,0)
ORANGE = (255, 66, 0)
PINK = (255, 0, 255)
LIGHT_RED = (255, 100, 100)
LIGHT_BLUE = (59, 193, 255)
LIGHT_ORANGE = (255, 94, 0)

# pre-defining fonts for ease of use later as I will need to use a lot of draw_text feature therefore, I pre-defined the fonts designs#
pygame.font.init()
SMALL_FONT = pygame.font.SysFont('comicsans', 25)
MEDIUM_FONT = pygame.font.SysFont('comicsans', 35)
BIG_FONT = pygame.font.SysFont('comicsans', 50)
HUGE_FONT = pygame.font.SysFont('comicsans', 80)


pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512) # Defining sound frequency, size and buffer #