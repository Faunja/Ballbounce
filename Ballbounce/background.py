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

def draw_text_background(tabbed, shift):
	if tabbed == False:
		draw_text("Tab - Hide Instructions", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16)])
		if shift == False:
			draw_text("Left Click - Grab Ball", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 2])
			draw_text("Right Click - Sling Ball", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 3])
		else:
			draw_text("Left Click - Pull Balls", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 2])
			draw_text("Right Click - Push Balls", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 3])
		draw_text("Shift - Change Mouse Mode", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 4])
		draw_text("WASD / Arrow Keys - Change Gravity", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 5])
		draw_text("Space Bar - Toggle Gravity", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 6])
		draw_text("R key - Reset Balls", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16) * 7])
	else:
		draw_text("Tab - Show Instructions", [round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 16)])
