# ball.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame, math, random
from defineball import *

def create_ball():
	mouse_x, mouse_y = pygame.mouse.get_pos()
	can_create = True
	for sphere in Dictionary.dictionary:
		if (math.sqrt((sphere.position[0] - mouse_x)**2 + (sphere.position[1] - mouse_y)**2) <= sphere.radius * 2):
			can_create = False
	if can_create == True:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
		for information in range(len(Dictionary.dictionary)):
			if Dictionary.dictionary[information].color == newcolor:
				newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
				information = 0
		Dictionary.dictionary.append(Circle(newcolor, mouse_x, mouse_y))

def delete_ball(cull = False):
	if cull == False:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		for sphere in Dictionary.dictionary:
			if (math.sqrt((sphere.position[0] - mouse_x)**2 + (sphere.position[1] - mouse_y)**2) <= sphere.radius):
				Dictionary.dictionary.remove(sphere)
				break
	else:
		if len(Dictionary.dictionary) != 0:
			del Dictionary.dictionary[random.randrange(len(Dictionary.dictionary))]
		
def update_ball(sphere):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	can_collide = False
	for cylinder in Dictionary.dictionary:
		if can_collide == True:
			sphere.ball_collision(cylinder)
		if cylinder.color == sphere.color:
			can_collide = True
	sphere.movement(mouse_x, mouse_y)
	sphere.collision()

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
			




