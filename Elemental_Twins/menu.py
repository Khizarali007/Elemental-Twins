# Importing necessary libraries and modules #
import pygame
import sys
from gui import *

class Menu:
	def __init__(self, surface):
# Constructor for the Menu class #
		self.surface = surface # The pygame surface (screen) on which to draw the menu #
# Load the menu background image, scaling it to the size of the game screen #
		self.background = pygame.transform.scale(pygame.image.load('Assets/background.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))


	def update(self):
# Method to update the menu screen #
		self.surface.blit(self.background, (0,0)) # Drawing the background image at the top-left corner blit draws the image #
# Display the 'Play' button. If it's clicked, return 'game' indicating the game should start
		if button(self.surface, 'Play', y=SCREEN_HEIGHT//2, color=BLUE, highlight_color=LIGHT_BLUE):
			return 'game'
# Display the 'Quit' button. If it's clicked, quit the game
		if button(self.surface, 'Quit', y=SCREEN_HEIGHT//2+100, color=ORANGE, highlight_color=LIGHT_ORANGE):
			pygame.quit()
			sys.exit()
 # Display the game TITLE at a predefined position using custom draw_text function
		draw_text(self.surface, TITLE, HUGE_FONT, color=WHITE, y=100)
