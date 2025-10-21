from settings import *
from sprite import Sprite

class Door(Sprite): # Initiating a Subclass Door from the Class Sprite #
	def __init__(self, x, y, path_close, path_open): # defines image paths for when doors are open and closed #
		self.rect = pygame.Rect(x, y, TILE_SIZE*2, TILE_SIZE*2)
		self.rect.x -= TILE_SIZE//2
		self.close_image = self._load_image(path_close) # loads the path_close image #
		self.open_image = self._load_image(path_open) # loads the path_open image #
		self.is_open = False

	def open(self):
		self.is_open = True

	def draw(self, surface): 
		if self.is_open:  # loads the image according to the if condition if door is open then the open door sprite is loaded
			surface.blit(self.open_image, self.rect)
		else: # else the close door sprite is loaded
			surface.blit(self.close_image, self.rect)

	def update(self, is_open):
		if is_open: # if statement to check if the door is open if it is it loads the self.open which loads open door sprite #
			self.open()

	def is_player_in(self, player):
		# return True if the door is open and the player is in front of it
		return self.is_open and player.rect.collidepoint(self.rect.center)
