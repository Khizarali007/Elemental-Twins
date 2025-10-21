from settings import *
from sprite import Sprite

# Creating Water Tiles ----------------------------------------#

class Water(Sprite): # Initiates a Subclass Water from the class Sprite #
	def __init__(self, x, y):
		super().__init__(x, y, TILE_SIZE, TILE_SIZE, "Assets/water.png") # Sprite is been implemented --#
