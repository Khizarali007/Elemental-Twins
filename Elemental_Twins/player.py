import pygame
from settings import *
from sprite import Sprite

class Player(Sprite):
	def __init__(self, x, y, image_path, keys):
# Initialize the Player object as a subclass of Sprite #
		super().__init__(x, y, TILE_SIZE*1.4, TILE_SIZE*1.4, image_path)
		self.right_image = self.image  # Store the right-facing image #
		self.left_image = pygame.transform.flip(self.image, True, False) # Create and store a left-facing image by flipping #
		self.pos = pygame.Vector2(x, y) # stores the player position (float) #
		self.keys = keys
		self.velocity = pygame.Vector2(0, 0)
		self.moving_speed = 2.5 # Horizontal speed of the player #
		self.jump_height = 8
		self.gravity = 0.4 # gravity force (will be added to vertical velocity each frame) # 
		self.on_ground = False # Boolean to check if player is on the ground #
		self.alive = True # Boolean to check if player is alive #

	def move(self, obstacles):
		keys_pressed = pygame.key.get_pressed() # Get state of all keyboard buttons # 

		# horizontal movement
		self.velocity.x = 0 # Resets horizontal velocity to zero
		if self.alive and keys_pressed[self.keys["right"]]: # right movement #
			self.velocity.x += self.moving_speed
			self.image = self.right_image # Update image to right-facing #


		if self.alive and keys_pressed[self.keys["left"]]: # left movement #
			self.velocity.x -= self.moving_speed
			self.image = self.left_image # Update image to left-facing #

		self.pos.x += self.velocity.x # Update horizontal position
		self.rect.x = self.pos.x # Update the rectangle's position for collision detection #
		collided_rect = self.get_collided_sprite_rect(obstacles) # Checks for collision #

# Correcting the position after horizontal collision #
		if collided_rect:
			if self.velocity.x > 0:
				self.rect.right = collided_rect.left
			elif self.velocity.x < 0:
				self.rect.left = collided_rect.right
			self.pos.x = self.rect.x

		# vertical movement
		self.velocity.y += self.gravity
		if self.alive and self.on_ground and keys_pressed[self.keys["up"]]:
			self.velocity.y = -self.jump_height
		self.pos.y += self.velocity.y
		self.rect.y = self.pos.y # Update rectangle's position for collision detection #
		collided_rect = self.get_collided_sprite_rect(obstacles) # Checks for collision #

# Correcting the position after vertical collision #	
		if collided_rect:
			if self.velocity.y > 0: # Falling down
				self.rect.bottom = collided_rect.top
				self.on_ground = True # Moving up
			elif self.velocity.y < 0:
				self.rect.top = collided_rect.bottom
			self.velocity.y = 0 # Stops vertical movement #
			self.pos.y = self.rect.y
		else:
			self.on_ground = False

	def update(self, obstacles):
		# Calls the move method within update to handle player movement
		self.move(obstacles)


