import pygame
from settings import *
from sprite import Sprite
from time import time

class Gun(Sprite):
	def __init__(self, x, y, direction, type, fire_rate=2): 

		right = 1 
		left = -1
# Defining right and left #
		if direction == 1:                                             # if it is right then image from this path would be loaded ----#
			path = "assets/cannon_right.png"
		elif direction == -1:                                          # if the gun is left then image from this path would be loaded #
			path = "assets/cannon_left.png"
		if type == MAP_FIRE_GUN_RIGHT or type == MAP_FIRE_GUN_LEFT:
			self.color = RED                                               # bullet colour would be red if it is lava gun ------------#
		elif type == MAP_WATER_GUN_RIGHT or type == MAP_WATER_GUN_LEFT:
			self.color = BLUE                                              # bullet colour would be blue if it is water gun ----------#
		else:
			self.color = YELLOW                                            # bullet colour would be yellow if it is none of the above #

		super().__init__(x, y, TILE_SIZE, TILE_SIZE, path)
		self.direction = direction
		self.fire_rate = fire_rate # seconds
		self.bullets = []
		self.last_shot = time()
# defining the direction, fire rate the sprite from level file and the last shot time here #
	def shoot(self):
		self.bullets.append(Bullet(self.rect.centerx, self.rect.centery, self.direction, self.color))
		self.last_shot = time()

	def draw(self, surface):
# draws bullet onto the screen #
		for bullet in self.bullets:
			bullet.draw(surface)
		super().draw(surface)

	def update(self, obstacles): # updates the bullet each frame and checks if the last bullet shot time is more than fire rate is yes it
# shoots the next bullet #
		"""obstacles: list of sprites that destroy bullets"""
		if time() - self.last_shot >= self.fire_rate:
			self.shoot()

		for bullet in self.bullets:
			bullet.update()

			if bullet.out_of_screen() or bullet.collide(obstacles):
				self.bullets.remove(bullet)
# removes bullet incase they go out of screen #

class Bullet:
	def __init__(self, x, y, direction, color): # initialises bullet class #
		self.rect = pygame.Rect(0, 0, TILE_SIZE // 3, TILE_SIZE // 3) # Create a rectangle for the bullet, 1/3 the size of a tile #
		self.radius = self.rect.w // 2 + 1 # Calculate the bullet's radius for drawing it as a circle #
		self.rect.center = (x, y) # Set the bullet's starting position #
		self.x = x # Store the bullet's x-coordinate #
		self.color = color # Set the bullet's color #
		self.direction = direction # Direction the bullet is moving: 1 for right, -1 for left #
		self.bullet_speed = 2 # Set the bullet's speed #

	def out_of_screen(self):
# Checks if the bullet is outside the screen bounds #
		if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
			return True
		return False

	def collide(self, obstacles): 
# Checks if the bullet has collided with any obstacles #
		for obstacle in obstacles:
			if self.rect.colliderect(obstacle.rect):
				return True
		return False

	def update(self):
# Updates the bullet's position #
		self.x += self.direction * self.bullet_speed # Moves the bullet in its direction by its speed #
		self.rect.x = self.x # Update the bullet's rectangle position #

	def draw(self, surface):
# Draws the bullet on the screen
		pygame.draw.circle(surface, self.color, self.rect.center, self.radius)
