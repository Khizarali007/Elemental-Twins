import pygame

class Sprite:
	def __init__(self, x, y, w, h, path):
		self.rect = pygame.Rect(x, y, w, h) # stores the sprite position (int) and size
		self.image = self._load_image(path)


	def _load_image(self, path):
		image = pygame.image.load(path).convert_alpha()
		image = pygame.transform.scale(image, (self.rect.w, self.rect.h))
		return image

	def draw(self, screen):
		rect = self.rect.copy()
		rect.x = self.rect.x
		rect.y = self.rect.y
		# draws the image at the center of the rect
		screen.blit(self.image, (rect.centerx - self.image.get_width()//2, rect.centery - self.image.get_height()//2))

	def get_collided_sprite_rect(self, sprites): # returns the rect of the obstacle self.rect collided with
		for obstacle in sprites:
			if self.rect.colliderect(obstacle.rect):
				return obstacle.rect
		return None

