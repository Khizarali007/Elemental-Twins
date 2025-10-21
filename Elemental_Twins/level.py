from door import Door
from lava import Lava
from settings import *
from wall import Wall
from player import Player
from gem import Gem
from water import Water
from gun import Gun
from time import time
from gui import draw_text

class Level:
	def __init__(self, map_name):
		level_data = self.read_level(map_name) # reads data from map files #

		self.create_level(level_data)
		self.completed = False # sets the level completed to false at start #
		self.start_time = time() # initialises time #
		self.current_time = 0

	def read_level(self, map_name):
		# Read level data from file
		with open(map_name, 'r') as f:
			level_data = []
			for line in f:
				line = line.strip()
				if line and line[0] != '#':  # ignore blank lines and comments
					level_data.append(line)
		return level_data

	def create_level(self, level_data): # Based on the loaded level data, it creates game objects such as players, walls and guns, etc.
		self.walls_sprites = []
		self.lava_sprites = []
		self.water_sprites = []
		self.gun_sprites = []
		self.fire_gun_sprites = []
		self.water_gun_sprites = []
		self.water_gems = []
		self.lava_gems = []
		self.lava_door = None
		self.water_door = None
		# Create level from level data
		for y, row in enumerate(level_data):
			for x, char in enumerate(row):
				if char == MAP_PLAYER1:
					self.player1 = Player(x=x*TILE_SIZE, y=y*TILE_SIZE, image_path="assets/player1.png", keys=PLAYER1_KEYS)
				elif char == MAP_PLAYER2:
					self.player2 = Player(x=x*TILE_SIZE, y=y*TILE_SIZE, image_path="assets/player2.png", keys=PLAYER2_KEYS)
				elif char == MAP_WALL:
					self.walls_sprites.append(Wall(x * TILE_SIZE, y * TILE_SIZE))
				elif char == MAP_LAVA:
					self.lava_sprites.append(Lava(x * TILE_SIZE, y * TILE_SIZE))
				elif char == MAP_WATER:
					self.water_sprites.append(Water(x * TILE_SIZE, y * TILE_SIZE))
				elif char == MAP_LAVA_GEM:
					self.lava_gems.append(Gem(x * TILE_SIZE, y * TILE_SIZE, type=MAP_LAVA_GEM))
				elif char == MAP_WATER_GEM:
					self.water_gems.append(Gem(x * TILE_SIZE, y * TILE_SIZE, type=MAP_WATER_GEM))
				elif char == MAP_LAVA_DOOR:
					self.lava_door = Door(x * TILE_SIZE, y * TILE_SIZE, path_close="assets/lava_door.png", path_open="assets/lava_door_open.png")
				elif char == MAP_WATER_DOOR:
					self.water_door = Door(x * TILE_SIZE, y * TILE_SIZE, path_close="assets/water_door.png", path_open="assets/water_door_open.png")

				elif char == MAP_GUN_RIGHT:
					self.gun_sprites.append(Gun(x * TILE_SIZE, y * TILE_SIZE, direction=1, type=MAP_GUN_RIGHT))
				elif char == MAP_GUN_LEFT:
					self.gun_sprites.append(Gun(x * TILE_SIZE, y * TILE_SIZE, direction=-1, type=MAP_GUN_LEFT))
				elif char == MAP_FIRE_GUN_RIGHT:
					self.fire_gun_sprites.append(Gun(x * TILE_SIZE, y * TILE_SIZE, direction=1, type=MAP_FIRE_GUN_RIGHT))
				elif char == MAP_FIRE_GUN_LEFT:
					self.fire_gun_sprites.append(Gun(x * TILE_SIZE, y * TILE_SIZE, direction=-1, type=MAP_FIRE_GUN_LEFT))
				elif char == MAP_WATER_GUN_RIGHT:
					self.water_gun_sprites.append(Gun(x * TILE_SIZE, y * TILE_SIZE, direction=1, type=MAP_WATER_GUN_RIGHT))
				elif char == MAP_WATER_GUN_LEFT:
					self.water_gun_sprites.append(Gun(x * TILE_SIZE, y * TILE_SIZE, direction=-1, type=MAP_WATER_GUN_LEFT))

	def draw_time(self, surface): # using the draw_time function #
		if self.completed: # if level is completed #
			font = BIG_FONT # then use the big font defined in the settings #
			pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//3) # draw it on this position #
		else: 
			font = MEDIUM_FONT # if not then use the medium font #
			pos = (SCREEN_WIDTH//2, 20) # on this position #
		draw_text(surface, f"Time: {int(self.current_time)}", font, x=pos[0], y=pos[1]) # Display the text "Time" and then the current time #

	def draw(self, surface):
		# draws walls
		for wall in self.walls_sprites:
			wall.draw(surface)
		# draws doors
		self.lava_door.draw(surface)
		self.water_door.draw(surface)
		# draws players
		self.player1.draw(surface)
		self.player2.draw(surface)
		# draws lava
		for lava in self.lava_sprites:
			lava.draw(surface)
		# draws water
		for water in self.water_sprites:
			water.draw(surface)
		# draws gems
		for gem in self.lava_gems + self.water_gems:
			gem.draw(surface)
		# draws guns
		for gun in self.gun_sprites + self.fire_gun_sprites + self.water_gun_sprites: # for all three water, lava and normal gun draws them #
			gun.draw(surface)

		self.draw_time(surface)


	def update(self):
		if self.completed: # if the level is completed, don't update anything
			return
		# updates timer
		if self.player1.alive and self.player2.alive: # Checks if player 1 and player 2 are alive #
			self.current_time = time() - self.start_time # updates the timer by subtracting initial time from current time #

		# updates players
		players_obstacles = self.walls_sprites + self.gun_sprites + self.fire_gun_sprites + self.water_gun_sprites # If they touched obstacles #
		if not self.player1.alive or not self.player2.alive: # if one of the players is dead, also kill the other one
			self.player2.alive = False # player 2 dies #
			self.player1.alive = False # player 1 dies #
		self.player1.update(obstacles=players_obstacles + [self.player2]) # updates upon collision with anything or the other player #
		self.player2.update(obstacles=players_obstacles + [self.player1]) # updates upon collision with anything or the other player #
		# updates water
		for water in self.water_sprites:
			if self.player1.rect.colliderect(water.rect): # If player 1 red player touches the water #
				self.player1.alive = False # player dies #
		# updates lava
		for lava in self.lava_sprites: 
			if self.player2.rect.colliderect(lava.rect): # If player 2 blue player touches the lava #
				self.player2.alive = False # player dies #
		# updates gems
		for gem in self.lava_gems:
			if self.player1.rect.colliderect(gem.rect): # If the player 1 red player collides with lava gem #
				self.lava_gems.remove(gem) # gem is removed from the map #
		for gem in self.water_gems:
			if self.player2.rect.colliderect(gem.rect): # If the player 2 blue player collides with water gem #
				self.water_gems.remove(gem) # gem is removed from the map #

		# updates doors
		self.lava_door.update(is_open=len(self.lava_gems) == 0) 
# it updates the lava door and sets it to is_open if the length of array that stores the lava gems is equal to 0 #
		self.water_door.update(is_open=len(self.water_gems) == 0)
# it updates the water door and sets it to is_open if the length of array that stores the water gems is equal to 0 #
		if self.lava_door.is_player_in(self.player1) and self.water_door.is_player_in(self.player2):
# Checks if both the red player is on the lava door and if blue player is on the water door if both conditions are true #
			self.completed = True # level is completed #

		# updates guns
		for gun in self.gun_sprites:
			gun.update(obstacles=self.walls_sprites)
			if self.player1.get_collided_sprite_rect(gun.bullets): # If player 1 collides with normal bullets #
				self.player1.alive = False # player 1 dies #
			if self.player2.get_collided_sprite_rect(gun.bullets): # If player 2 collides with normal bullets #
				self.player2.alive = False # player 2 dies #
		# updates fire guns
		for gun in self.fire_gun_sprites: # this is the fire gun #
			gun.update(obstacles=self.walls_sprites+self.gun_sprites+[self.player1])
			if self.player2.get_collided_sprite_rect(gun.bullets):
				self.player2.alive = False # Only if player 2 water player touches lava gun it dies #
		# updates water guns
		for gun in self.water_gun_sprites: # this is the water gun #
			gun.update(obstacles=self.walls_sprites+self.gun_sprites+[self.player2])
			if self.player1.get_collided_sprite_rect(gun.bullets):
				self.player1.alive = False # Only if player 1 lava player touches water gun it dies #


