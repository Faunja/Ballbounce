# ball.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame, math, random
from defineball import *

def grab_ball(click):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for sphere in dictionary:
		if click == True and sphere.held == False:
			if (math.sqrt((sphere.x[0] - mouse_x)**2 + (sphere.y[0] - mouse_y)**2) <= sphere.radius):
				sphere.held = True
		if click == False and sphere.held == True:
			sphere.held = False

def sling_ball(click):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for sphere in dictionary:
		if click == True and sphere.sling == False:
			if (math.sqrt((sphere.x[0] - mouse_x)**2 + (sphere.y[0] - mouse_y)**2) <= sphere.radius):
				sphere.sling = True
		if click == False and sphere.sling == True:
			sphere.sling = False

def stop_ball():
	for sphere in dictionary:
		sphere.x[1] = 0
		sphere.y[1] = 0
		
def random_ball():
	for sphere in dictionary:
		sphere.x[1] += random.randint(-100, 100)
		sphere.y[1] += random.randint(-100, 100)

def draw_ball():
	create_ball(16)
	slinged = None
	for sphere in dictionary:
		update_ball(sphere)
		pygame.draw.circle(screen, (0, 0, 0), (sphere.x[0], sphere.y[0]), sphere.radius)
		pygame.draw.circle(screen, sphere.color, (sphere.x[0], sphere.y[0]), sphere.radius * (4 / 5))
		if sphere.sling == True:
			slinged = sphere
	if slinged != None:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		pygame.draw.circle(screen, (0, 0, 0), (mouse_x, mouse_y), slinged.radius / 2)
		pygame.draw.circle(screen, slinged.color, (mouse_x, mouse_y), slinged.radius * (4 / 10))
			




