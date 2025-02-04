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
		if len(dictionary) == 0:
			self.direction = 3
		else:
			self.direction = dictionary[0].direction
		self.gravity = [None, None]
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
	
	def gravity_check(self):
		if self.pull == True:
			self.gravity[0], self.gravity[1] = pygame.mouse.get_pos()
		if self.push == True:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			difference = [mouse_x - self.position[0], mouse_y - self.position[1]]
			self.gravity[0] = self.position[0] - difference[0]
			self.gravity[1] = self.position[1] - difference[1]
		if self.pull == False and self.push == False:
			if self.direction == 1:
				self.gravity = [None, 0]
			elif self.direction == 2:
				self.gravity = [SCREEN_WIDTH, None]
			elif self.direction == 3:
				self.gravity = [None, SCREEN_HEIGHT]
			elif self.direction == 4:
				self.gravity = [0, None]
			else:
				self.gravity = [None, None]
	
	def gravity_movement(self):
		if self.gravity[0] != None and self.gravity[1] == None:
			if self.position[0] < self.gravity[0]:
				self.velocity[0] += 5
			elif self.position[0] > self.gravity[0]:
				self.velocity[0] -= 5
		elif self.gravity[1] != None and self.gravity[0] == None:
			if self.position[1] < self.gravity[1]:
				self.velocity[1] += 5
			elif self.position[1] > self.gravity[1]:
				self.velocity[1] -= 5
		elif self.gravity[0] != None and self.gravity[1] != None:
			difference = [self.gravity[0] - self.position[0], self.gravity[1] - self.position[1]]
			x_push = 5 * abs(difference[0] / difference[1])
			y_push = 5 * abs(difference[1] / difference[0])
			if x_push > 5:
				x_push = 5
			if y_push > 5:
				y_push = 5
			if self.position[0] < self.gravity[0]:
				self.velocity[0] += x_push
			elif self.position[0] > self.gravity[0]:
				self.velocity[0] -= x_push
			if self.position[1] < self.gravity[1]:
				self.velocity[1] += y_push
			elif self.position[1] > self.gravity[1]:
				self.velocity[1] -= y_push

	def movement(self, mouse_x, mouse_y):
		if numpy.isnan(self.position[0]) == True or numpy.isnan(self.position[1]) == True:
			self.position = numpy.array([random.randrange(self.radius, SCREEN_WIDTH), random.randrange(self.radius, SCREEN_HEIGHT)])
			while self.check_ball_collision == True:
				self.position = numpy.array([random.randrange(self.radius, SCREEN_WIDTH), random.randrange(self.radius, SCREEN_HEIGHT)])
			self.velocity = numpy.array([0.0, 0.0])
		else:
			if self.held == True:
				self.velocity[0] = mouse_x - self.position[0]
				self.position[0] = mouse_x
				self.velocity[1] = mouse_y - self.position[1]
				self.position[1] = mouse_y
			elif self.sling == True:
				self.velocity[0] = (mouse_x - self.position[0]) / self.friction
				self.velocity[1] = (mouse_y - self.position[1]) / self.friction
			else:
				self.gravity_check()
				self.gravity_movement()
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
		if self.held == True or self.sling == True:
			sphere.position = sphere.position - difference * offset
		elif sphere.held == True or sphere.sling == True:
			self.position = self.position + difference * offset
		else:
			self.position = self.position + difference * offset
			sphere.position = sphere.position - difference * offset

		if self.sling == False and sphere.sling == False:
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




