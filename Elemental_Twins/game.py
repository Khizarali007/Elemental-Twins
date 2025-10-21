from level import Level
from settings import *
from gui import *

class Game:
	def __init__(self, surface): # Initialising the class Game with 2 arguments #
		self.surface = surface
		self.background = pygame.transform.scale(pygame.image.load('Assets/background.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
# loading the background image on the map and scaling it upto the same size as the game window #
		self.levels_names = ('maps/map1.txt', 'maps/map2.txt', 'maps/map3.txt', 'maps/map4.txt', 'maps/map5.txt', 'maps/victory.txt')
# loads the maps (text files) in order from the maps folder #
		self.current_level_index = 0
		self.current_level = Level(self.levels_names[self.current_level_index])
# creating a variable to keep the current level index so that we can then compare it with total index and decide if user has completed
# all the levels #
		
	def draw(self):
		self.surface.blit(self.background, (0,0)) # loading background image from 0,0 x and y axis top left corner #
		self.current_level.draw(self.surface)

	def update(self): # updates everything given below once every frame #
		self.draw()
		self.current_level.update()
		# make the level change when it's completed
		if self.current_level.completed:
			if self.current_level_index < len(self.levels_names) - 1: # checks if level is completed and if it is not the last level #

				draw_text(self.surface, 'Level completed', BIG_FONT, color=GREEN)
				draw_text(self.surface, 'Press Space to continue', BIG_FONT, y=SCREEN_HEIGHT//2+50)

				if pygame.key.get_pressed()[pygame.K_SPACE]: # Checks if user has pressed Space #
					self.current_level_index += 1
					self.current_level = Level(self.levels_names[self.current_level_index]) # Moves forward to next level #
			else: # if there are no more levels

				draw_text(self.surface, 'You Won!', BIG_FONT, color=GREEN)
				draw_text(self.surface, 'Press Space to return to the menu', BIG_FONT, y=SCREEN_HEIGHT//2+50)

				if pygame.key.get_pressed()[pygame.K_SPACE]: # If it is last level and completed Pressing Space would return the game to menu #
					return 'menu'
		# game over
		elif not self.current_level.player1.alive or not self.current_level.player2.alive:

			draw_text(self.surface, 'Game Over', BIG_FONT, color=RED)
			draw_text(self.surface, 'Press Space to restart the level', BIG_FONT, y=SCREEN_HEIGHT//2+50)
# If the players die this text would pop up on the screen #
			if pygame.key.get_pressed()[pygame.K_SPACE]:
				self.current_level = Level(self.levels_names[self.current_level_index])
