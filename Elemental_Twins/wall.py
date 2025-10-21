from settings import *
from sprite import Sprite

# Creating Walls ----------------------------------------------------------------------------------------#

class Wall(Sprite): # Initiates a Subclass Wall from the class Sprite -----------------------------------#
	def __init__(self, x, y):
		super().__init__(x, y, TILE_SIZE, TILE_SIZE, "Assets/wall2.png") # Sprite has been implemented --#
