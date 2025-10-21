from settings import *
from sprite import Sprite

# Creating Lava Tile ------------------------------------------#

class Lava(Sprite): # Initiates a Subclass Lava from the class Sprite #
	def __init__(self, x, y):
		super().__init__(x, y, TILE_SIZE, TILE_SIZE, "Assets/lava.png") # Sprite has been implemented --#
