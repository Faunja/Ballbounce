# ball.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame, math, random
from defineball import *

def grab_ball(click):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for sphere in Dictionary.dictionary:
		if click == True and sphere.held == False:
			if (math.sqrt((sphere.position[0] - mouse_x)**2 + (sphere.position[1] - mouse_y)**2) <= sphere.radius):
				sphere.held = True
				break
		if click == False and sphere.held == True:
			sphere.held = False

def sling_ball(click):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for sphere in Dictionary.dictionary:
		if click == True and sphere.sling == False:
			if (math.sqrt((sphere.position[0] - mouse_x)**2 + (sphere.position[1] - mouse_y)**2) <= sphere.radius):
				sphere.sling = True
				break
		if click == False and sphere.sling == True:
			sphere.sling = False

def draw_ball():
	mouse_x, mouse_y = pygame.mouse.get_pos()
	slinged = None
	for sphere in Dictionary.dictionary:
		if sphere.pull == True or sphere.push == True:
			pygame.draw.circle(screen, White, (sphere.position[0], sphere.position[1]), sphere.radius)
			pygame.draw.circle(screen, sphere.color, (sphere.position[0], sphere.position[1]), sphere.radius * (4 / 5))
		else:
			pygame.draw.circle(screen, sphere.color, (sphere.position[0], sphere.position[1]), sphere.radius)
		if sphere.sling == True:
			slinged = sphere
		sphere.movement(mouse_x, mouse_y)
	if slinged != None:
		pygame.draw.circle(screen, slinged.color, (mouse_x, mouse_y), slinged.radius / 2)
			




