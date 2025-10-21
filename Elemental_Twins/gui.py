import pygame
from settings import *

def draw_text(surface, text, font, color=WHITE, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2):
	text_obj = font.render(text, 1, color)
	text_rect = text_obj.get_rect()
	text_rect.center = (x, y)
	surface.blit(text_obj, text_rect)


def button(surface, text, font=BIG_FONT, width=150, height=75, color=GREY, highlight_color=WHITE,
		   x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2, text_color=BLACK):
	rect = pygame.Rect(x-width//2, y-height//2, width, height)
	mouse_pos = pygame.mouse.get_pos()
	mouse_clicked = pygame.mouse.get_pressed()[0]
	if rect.collidepoint(mouse_pos):
		color = highlight_color
		if mouse_clicked:
			return True
	pygame.draw.rect(surface, color, rect, border_radius=16)
	draw_text(surface, text, font, text_color, rect.centerx, rect.centery)
