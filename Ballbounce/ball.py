# ball.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame, math, random
from defineball import *

dictionary = []
color_dictionary = []

def stop_ball():
	for sphere in dictionary:
		sphere.x[1] = 0
		sphere.y[1] = 0
		
def random_ball():
	for sphere in dictionary:
		sphere.x[1] += random.randint(-1000, 1000)
		sphere.y[1] += random.randint(-1000, 1000)

def grab_ball(click):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for sphere in dictionary:
		if click == True and sphere.held == False:
			if (math.sqrt((sphere.x[0] - mouse_x)**2 + (sphere.y[0] - mouse_y)**2) <= sphere.radius):
				sphere.held = True
		if click == False and sphere.held == True:
			sphere.held = False

# Do not put count above 30 untill I fix this shit.
# The issue lies within the define ball file in the ball collision function.
def create_ball(count):
	while len(dictionary) < count:
		newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
		for information in range(len(color_dictionary)):
			if color_dictionary[information] == newcolor:
				newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
				information = 0
		dictionary.append(Circle(newcolor))
		color_dictionary.append(newcolor)

def update_ball(sphere):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for other in dictionary:
		if other.color != sphere.color:
			sphere.ball_collision(other)
	sphere.movement(mouse_x, mouse_y)
	sphere.collision()

def draw_ball():
	create_ball(20)
	for sphere in dictionary:
		update_ball(sphere)
		pygame.draw.circle(screen, (0, 0, 0), (sphere.x[0], sphere.y[0]), sphere.radius)
		pygame.draw.circle(screen, sphere.color, (sphere.x[0], sphere.y[0]), sphere.radius * (4 / 5))
		
