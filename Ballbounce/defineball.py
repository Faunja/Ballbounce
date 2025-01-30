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
		self.velocity = numpy.array([0.0, 0.0])
		self.radius = SCREEN_HEIGHT / 24
		self.friction = .9
		self.gravity = [None, SCREEN_HEIGHT]
		self.held = False
		self.sling = False
		self.pull = False
		self.push = False
	
	def check_ball_collision(self, sphere):
		difference = self.position - sphere.position
		distance = math.sqrt(difference[0]**2 + difference[1]**2)
		push_radius = self.radius + sphere.radius
		if (distance <= push_radius):
			return True
		else:
			return False
	
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
			if self.pull == True:
				self.gravity[0], self.gravity[1] = pygame.mouse.get_pos()
			if self.push == True:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				difference = [mouse_x - self.position[0], mouse_y - self.position[1]]
				self.gravity[0] = self.position[0] - difference[0]
				self.gravity[1] = self.position[1] - difference[1]
			if self.pull == False and self.push == False:
				self.gravity = [None, SCREEN_HEIGHT]
			if self.gravity[0] != None:
				if self.position[0] < self.gravity[0]:
					self.velocity[0] += 5
				elif self.position[0] > self.gravity[0]:
					self.velocity[0] -= 5
			if self.gravity[1] != None:
				if self.position[1] < self.gravity[1]:
					self.velocity[1] += 5
				elif self.position[1] > self.gravity[1]:
					self.velocity[1] -= 5
			self.position[0] += self.velocity[0]
			self.velocity[0] *= self.friction
			self.position[1] += self.velocity[1]
			self.velocity[1] *= self.friction
	
	def collision(self):
		if self.position[0] - self.radius <= 0:
			self.position[0] = self.radius
			self.velocity[0] *= -self.friction
		elif self.position[0] + self.radius >= SCREEN_WIDTH:
			self.position[0] = SCREEN_WIDTH - self.radius
			self.velocity[0] *= -self.friction
		if self.position[1] - self.radius <= 0:
			self.position[1] = self.radius
			self.velocity[1] *= -self.friction
		elif self.position[1] + self.radius >= SCREEN_HEIGHT:
			self.position[1] = SCREEN_HEIGHT - self.radius
			self.velocity[1] *= -self.friction
	
	def ball_collision(self, sphere):
		if self.check_ball_collision(sphere) == False:
			return
		difference = self.position - sphere.position
		distance = math.sqrt(difference[0]**2 + difference[1]**2)
		push_radius = self.radius + sphere.radius
		offset = 1 - distance / push_radius
		if self.held == True:
			sphere.position = sphere.position - difference * offset
		elif sphere.held == True:
			self.position = self.position + difference * offset
		else:
			self.position = self.position + difference * offset
			sphere.position = sphere.position - difference * offset

		mass = [sphere.radius * 2 / (sphere.radius + self.radius), self.radius * 2 / (self.radius + sphere.radius)]
		selfposition = self.position - sphere.position
		sphereposition = sphere.position - self.position
		selfnumerator = numpy.inner(self.velocity - sphere.velocity, selfposition)
		spherenumerator = numpy.inner(sphere.velocity - self.velocity, sphereposition)
		selfdenominator = numpy.linalg.norm(selfposition) ** 2
		spheredenominator = numpy.linalg.norm(sphereposition) ** 2

		self.velocity = self.velocity - mass[0] * selfnumerator / selfdenominator * selfposition
		sphere.velocity = sphere.velocity - mass[1] * (spherenumerator / spheredenominator) * sphereposition

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




