from settings import *
from sprite import Sprite

class Gem(Sprite):
	def __init__(self, x, y, type):
		if type == MAP_LAVA_GEM:
			path = "assets/lava_gem.png"
		elif type == MAP_WATER_GEM:
			path = "assets/water_gem.png"
		super().__init__(x, y, TILE_SIZE, TILE_SIZE, path)
