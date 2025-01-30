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
			if (math.sqrt((sphere.position[0] - mouse_x)**2 + (sphere.position[1] - mouse_y)**2) <= sphere.radius):
				sphere.held = True
		if click == False and sphere.held == True:
			sphere.held = False

def sling_ball(click):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for sphere in dictionary:
		if click == True and sphere.sling == False:
			if (math.sqrt((sphere.position[0] - mouse_x)**2 + (sphere.position[1] - mouse_y)**2) <= sphere.radius):
				sphere.sling = True
		if click == False and sphere.sling == True:
			sphere.sling = False

def pull_ball(click):
	for sphere in dictionary:
		sphere.pull = click

def push_ball(click):
	for sphere in dictionary:
		sphere.push = click

def stop_ball():
	for sphere in dictionary:
		sphere.velocity[0] = 0
		sphere.velocity[1] = 0
		
def random_ball():
	for sphere in dictionary:
		sphere.velocity[0] += random.randint(-100, 100)
		sphere.velocity[1] += random.randint(-100, 100)

def draw_ball():
	slinged = None
	for sphere in dictionary:
		pygame.draw.circle(screen, sphere.color, (sphere.position[0], sphere.position[1]), sphere.radius)
		if sphere.sling == True:
			slinged = sphere
		update_ball(sphere)
	if slinged != None:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		pygame.draw.circle(screen, slinged.color, (mouse_x, mouse_y), slinged.radius / 2)
			




