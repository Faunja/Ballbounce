# ball.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame, math, random
from defineball import *
		
def update_ball(sphere):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	if Dictionary.collision == True:
		can_collide = False
		for cylinder in Dictionary.dictionary:
			if can_collide == True:
				sphere.ball_collision(cylinder)
			if cylinder.color == sphere.color:
				can_collide = True
	sphere.movement(mouse_x, mouse_y)
	sphere.wall_collision()

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
	slinged = None
	for sphere in Dictionary.dictionary:
		pygame.draw.circle(screen, sphere.color, (sphere.position[0], sphere.position[1]), sphere.radius)
		if sphere.sling == True:
			slinged = sphere
		update_ball(sphere)
	if slinged != None:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		pygame.draw.circle(screen, slinged.color, (mouse_x, mouse_y), slinged.radius / 2)
			




