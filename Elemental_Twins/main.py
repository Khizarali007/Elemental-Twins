# Importing necessary libraries and modules -------------------#
import pygame
import sys
import sound
from settings import * # Importing all variables/constants from settings.py ------------- #
from game import Game # Importing the Game class from game.py --------------------------- #
from menu import Menu # Importing the Menu class from menu.py --------------------------- #


# Setup pygame/window ---------------------------------------- #
pygame.init() # Initialize the pygame library #
pygame.display.set_caption(TITLE) # Set the window as TITLE as defined in settings.py --- #
# Creates a display window with dimensions and settings specified in settings.py -------- #
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)
mainClock = pygame.time.Clock()  # Clock object to control game frame rate -------------- #

# Game ------------------------------------------------------- #
state = 'menu' # Initialize the game state to 'menu' #
menu = Menu(SCREEN) # Create a Menu object passing the SCREEN as argument --------------- #

# Theme music -------------------------------------------------#
sound.sounds.play_background_music() # Play background music from the sound module ------ #

# Loop ------------------------------------------------------- #
while True: # Infinite loop to keep the game running ------------------------------------ # 
	for event in pygame.event.get(): # Loop through a list of captured events ----------- #
		if event.type == pygame.QUIT: # If the close button is clicked ------------------ #
			pygame.quit() # Uninitialize all pygame modules ----------------------------- #
			sys.exit() # Exit the script ------------------------------------------------ #
	if state == 'menu': # If the current state is 'menu' -------------------------------- #
		if menu.update() == 'game':  # Update the menu and check if the output is 'game'- #
			game = Game(SCREEN) # Create a Game object passing the SCREEN as argument --- #
			state = 'game' # Change the state to 'game' --------------------------------- #
	if state == 'game': # If the current state is 'game' -------------------------------- #
		if game.update() == 'menu': # Update the game and check if the output is 'menu' - #
			state = 'menu' # Change the state back to 'menu' ---------------------------- #

	pygame.display.update() # Updates the contents of the entire display ---------------- #
	mainClock.tick(FPS) # Runs at the frame rate as per FPS defined in settings.py ------ #
