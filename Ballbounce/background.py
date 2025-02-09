# background.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *

def draw_text(text, position):
	font = pygame.font.Font('m6x11.ttf', round(SCREEN_HEIGHT / 32))
	printed = font.render(text, True, White)
	printed_width, printed_height = printed.get_size()
	screen.blit(printed, (position[0] - printed_width / 2, position[1] - printed_height / 2))

def draw_text_background(tabbed, shift, space, friction, collision):
	if tabbed == False:
		draw_text("Tab - Hide Instructions", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16)])
		draw_text("Enter - Create Balls", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 2])
		draw_text("Backspace - Delete Balls", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 3])
		draw_text("R Key - Reset Balls", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 4])
		if friction != 1:
			draw_text("F Key - Disable Friction", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 5])
		else:
			draw_text("F Key - Enable Friction", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 5])
		if collision == True:
			draw_text("C Key - Disable Ball Collision", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 6])
		else:
			draw_text("C Key - Enable Ball Collision", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 6])
		if shift == False:
			draw_text("Shift - Enable Mouse Gravity", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 7])
			draw_text("Left Click - Grab Ball", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 8])
			draw_text("Right Click - Sling Ball", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 9])
		else:
			draw_text("Shift - Disable Mouse Gravity", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 7])
			draw_text("Left Click - Pull Balls", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 8])
			draw_text("Right Click - Push Balls", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 9])
		if space == False:
			draw_text("Space Bar - Disable Gravity", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 10])
			draw_text("WASD / Arrow Keys - Change Gravity", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 11])
		else:
			draw_text("Space Bar - Enable Gravity", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 10])
	else:
		draw_text("Tab - Show Instructions", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16)])
