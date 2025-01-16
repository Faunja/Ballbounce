# background.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame, random
from variables import *

colors = []

def search_color(x, y):
	for entries in colors:
		if entries[0] == x and entries[1] == y:
			return entries[2]
	offset = random.randint(0, 7)*3
	colors.append([x, y, offset])
	return offset

def pop_entry(min_x, max_x, min_y, max_y):
	for entries in colors:
		if entries[0] < min_x or entries[0] > max_x:
			colors.remove(entries)
		elif entries[1] < min_y or entries[1] > max_y:
			colors.remove(entries)

def draw_hexagon(x, y, size, offset = 0):
	red = [(255-offset, 45-offset, 45-offset), 
	(251-offset, 41-offset, 41-offset), 
	(247-offset, 37-offset, 37-offset), 
	(243-offset, 33-offset, 33-offset)]
	pygame.draw.polygon(screen, red[3], ((x, y), (-size[0]*2+x, y), (-size[0]+x, size[1]+y)))
	pygame.draw.polygon(screen, red[2], ((x, y), (-size[0]+x, size[1]+y), (size[0]+x, size[1]+y)))
	pygame.draw.polygon(screen, red[2], ((x, y), (-size[0]*2+x, y), (-size[0]+x, -size[1]+y)))
	pygame.draw.polygon(screen, red[1], ((x, y), (size[0]+x, size[1]+y), (size[0]*2+x, y)))
	pygame.draw.polygon(screen, red[1], ((x, y), (-size[0]+x, -size[1]+y), (size[0]+x, -size[1]+y)))
	pygame.draw.polygon(screen, red[0], ((x, y), (size[0]+x, -size[1]+y), (size[0]*2+x, y)))

def draw_ball_background():
	screen.fill((210, 0, 0))
	
	center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
	size = [SCREEN_HEIGHT/50, SCREEN_HEIGHT/25]
	spacing = [size[0]*3.6, size[1]*1.2]
	view = [round((SCREEN_HEIGHT)/size[0]/2), round((SCREEN_HEIGHT)/size[1])]
	if view[1]%2 != 0:
		view[1] += 1

	for x in range(-view[0], view[0]):
		input_x = center[0]+spacing[0]*x
		for y in range(-view[1], view[1], 2):
			input_y = center[1]+spacing[1]*(y+x%2)
			if -size[0]-spacing[0] < input_x < SCREEN_WIDTH+size[0]+spacing[0] and -size[1]-spacing[1] < input_y < SCREEN_HEIGHT+size[1]+spacing[1]:
				draw_hexagon(input_x, input_y, size, search_color(x, y))

def draw_upgrade_background():
	screen.fill((210, 0, 0))
	
	center = [SCREEN_WIDTH/2+Cx, SCREEN_HEIGHT/2+Cy]
	size = [SCREEN_HEIGHT/(perspective*50), SCREEN_HEIGHT/(perspective*25)]
	spacing = [size[0]*3.6, size[1]*1.2]
	view = [round((SCREEN_HEIGHT)/size[0]/2), round((SCREEN_HEIGHT)/size[1])]
	if view[1]%2 != 0:
		view[1] += 1
	adjust = [round(Cx/size[0]/3.6), round(Cy/size[1]/1.2)-round(Cy/size[1]/1.2)%2]
	
	pop_entry(-view[0]-adjust[0], view[0]-adjust[0], -view[1]-adjust[1], view[1]-adjust[1])
	for x in range(-view[0]-adjust[0], view[0]-adjust[0]):
		input_x = center[0]+spacing[0]*x
		for y in range(-view[1]-adjust[1], view[1]-adjust[1], 2):
			input_y = center[1]+spacing[1]*(y+x%2)
			if -size[0]-spacing[0] < input_x < SCREEN_WIDTH+size[0]+spacing[0] and -size[1]-spacing[1] < input_y < SCREEN_HEIGHT+size[1]+spacing[1]:
				draw_hexagon(input_x, input_y, size, search_color(x, y))
