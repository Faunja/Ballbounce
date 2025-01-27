# defineball.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import math, random, numpy
from variables import *

dictionary = []
color_dictionary = []

class Circle:
	def __init__(self, color, x_place, y_place):
		self.color = color
		self.position = numpy.array([x_place, y_place])
		self.velocity = numpy.array([0, 0])
		self.radius = SCREEN_HEIGHT / 16
		self.friction = 9
		self.held = False
		self.sling = False
	
	def movement(self, mouse_x, mouse_y):
		if self.held == True:
			self.velocity[0] = mouse_x - self.position[0]
			self.position[0] = mouse_x
			self.velocity[1] = mouse_y - self.position[1]
			self.position[1] = mouse_y
		elif self.sling == True:
			self.velocity[0] = (mouse_x - self.position[0]) / self.friction
			self.velocity[1] = (mouse_y - self.position[1]) / self.friction
		else:
			self.position[0] += self.velocity[0]
			self.velocity[0] *= self.friction / 10
			if -1 < self.velocity[0] < 1:
				self.velocity[0] = 0
			self.position[1] += self.velocity[1]
			self.velocity[1] *= self.friction / 10
			if -1 < self.velocity[1] < 1:
				self.velocity[1] = 0
	
	def collision(self):
		if self.position[0] - self.radius <= 0:
			self.position[0] = self.radius
			self.velocity[0] *= -1
		elif self.position[0] + self.radius >= SCREEN_WIDTH:
			self.position[0] = SCREEN_WIDTH - self.radius
			self.velocity[0] *= -1
		if self.position[1] - self.radius <= 0:
			self.position[1] = self.radius
			self.velocity[1] *= -1
		elif self.position[1] + self.radius >= SCREEN_HEIGHT:
			self.position[1] = SCREEN_HEIGHT - self.radius
			self.velocity[1] *= -1
	
	def ball_collision(self, sphere):
		x_diff = (self.position[0] - sphere.position[0])
		y_diff = (self.position[1] - sphere.position[1])
		distance = math.sqrt(x_diff**2 + y_diff**2)
		push_radius = self.radius + sphere.radius
		if (distance <= push_radius):
			mass = [sphere.radius * 2 / (sphere.radius + self.radius), self.radius * 2 / (self.radius + sphere.radius)]

			selfposition = self.position - sphere.position
			sphereposition = sphere.position - self.position
			selfnumerator = numpy.inner(self.velocity - sphere.velocity, selfposition)
			spherenumerator = numpy.inner(sphere.velocity - self.velocity, sphereposition)
			selfdenominator = numpy.linalg.norm(selfposition) ** 2
			spheredenominator = numpy.linalg.norm(sphereposition) ** 2

			self.velocity = self.velocity - mass[0] * selfnumerator / selfdenominator * selfposition
			sphere.velocity = sphere.velocity - mass[1] * (spherenumerator / spheredenominator) * sphereposition

# Do not put count above 4 untill I fix this.
# The issue lies within the ball collision function.
def create_ball():
	mouse_x, mouse_y = pygame.mouse.get_pos()
	can_create = True
	for sphere in dictionary:
		if (math.sqrt((sphere.position[0] - mouse_x)**2 + (sphere.position[1] - mouse_y)**2) <= sphere.radius * 2):
			can_create = False
	if can_create == True:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
		for information in range(len(color_dictionary)):
			if color_dictionary[information] == newcolor:
				newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
				information = 0
		dictionary.append(Circle(newcolor, mouse_x, mouse_y))
		color_dictionary.append(newcolor)

def delete_ball():
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for sphere in dictionary:
		if (math.sqrt((sphere.position[0] - mouse_x)**2 + (sphere.position[1] - mouse_y)**2) <= sphere.radius):
			color_dictionary.remove(sphere.color)
			dictionary.remove(sphere)
			break
		
def update_ball(sphere):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	can_collide = False
	for cylinder in dictionary:
		if can_collide == True:
			sphere.ball_collision(cylinder)
		if cylinder.color == sphere.color:
			can_collide = True
	sphere.movement(mouse_x, mouse_y)
	sphere.collision()




