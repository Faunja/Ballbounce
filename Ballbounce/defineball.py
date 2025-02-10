# defineball.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import math, random, numpy
from variables import *

class Global_Circle:
	def __init__(self):
		self.dictionary = []
		self.friction = .9
		self.gravity_pull = 5
		self.collision = True
		self.pull = False
		self.push = False
		self.space = False
		self.direction = 3

	def create_ball(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		can_create = True
		if self.collision == True:
			for sphere in self.dictionary:
				if (math.sqrt((sphere.position[0] - mouse_x)**2 + (sphere.position[1] - mouse_y)**2) <= sphere.radius * 2):
					can_create = False
		if can_create == True:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
			for information in range(len(self.dictionary)):
				if self.dictionary[information].color == newcolor:
					newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
					information = 0
			self.dictionary.append(Circle(newcolor, mouse_x, mouse_y))

	def delete_ball(self, cull = False):
		if cull == False:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			for sphere in self.dictionary:
				if (math.sqrt((sphere.position[0] - mouse_x)**2 + (sphere.position[1] - mouse_y)**2) <= sphere.radius):
					self.dictionary.remove(sphere)
					break
		else:
			if len(self.dictionary) != 1:
				initial_dictionary = len(self.dictionary)
				while round(initial_dictionary / 2) < len(self.dictionary):
					del self.dictionary[random.randrange(len(self.dictionary))]

Dictionary = Global_Circle()

class Circle:
	def __init__(self, color, x_place, y_place):
		self.color = color
		self.position = numpy.array([x_place, y_place])
		self.velocity = numpy.array([0.0, 0.0])
		self.radius = round(SCREEN_HEIGHT / 24)
		self.gravity = [None, None]
		self.held = False
		self.sling = False

	def check_wall_collision(self):
		if self.position[0] - self.radius <= 0:
			return True
		elif self.position[0] + self.radius >= SCREEN_WIDTH:
			return True
		if self.position[1] - self.radius <= 0:
			return True
		elif self.position[1] + self.radius >= SCREEN_HEIGHT:
			return True
		return False

	def check_ball_collision(self, sphere = None):
		if sphere != None:
			difference = self.position - sphere.position
			distance = math.sqrt(difference[0]**2 + difference[1]**2)
			push_radius = self.radius + sphere.radius
			if (distance <= push_radius):
				return True
			else:
				return False
		else:
			for sphere in Dictionary.dictionary:
				difference = self.position - sphere.position
				distance = math.sqrt(difference[0]**2 + difference[1]**2)
				push_radius = self.radius + sphere.radius
				if (distance <= push_radius):
					return True
			return False

	def gravity_check(self):
		if Dictionary.pull == True:
			self.gravity[0], self.gravity[1] = pygame.mouse.get_pos()
		if Dictionary.push == True:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			difference = [mouse_x - self.position[0], mouse_y - self.position[1]]
			self.gravity[0] = self.position[0] - difference[0]
			self.gravity[1] = self.position[1] - difference[1]
		if Dictionary.pull == False and Dictionary.push == False:
			if Dictionary.space == False:
				if Dictionary.direction == 1:
					self.gravity = [None, 0]
				elif Dictionary.direction == 2:
					self.gravity = [SCREEN_WIDTH, None]
				elif Dictionary.direction == 3:
					self.gravity = [None, SCREEN_HEIGHT]
				else:
					self.gravity = [0, None]
			else:
				self.gravity = [None, None]
	
	def gravity_movement(self):
		if self.gravity[0] != None and self.gravity[1] == None:
			if self.position[0] < self.gravity[0]:
				self.velocity[0] += Dictionary.gravity_pull
			elif self.position[0] > self.gravity[0]:
				self.velocity[0] -= Dictionary.gravity_pull
		elif self.gravity[1] != None and self.gravity[0] == None:
			if self.position[1] < self.gravity[1]:
				self.velocity[1] += Dictionary.gravity_pull
			elif self.position[1] > self.gravity[1]:
				self.velocity[1] -= Dictionary.gravity_pull
		elif self.gravity[0] != None and self.gravity[1] != None:
			difference = [self.gravity[0] - self.position[0], self.gravity[1] - self.position[1]]
			if difference[1] != 0:
				x_push = Dictionary.gravity_pull * abs(difference[0] / difference[1])
				if x_push > Dictionary.gravity_pull:
					x_push = Dictionary.gravity_pull
				if self.position[0] < self.gravity[0]:
					self.velocity[0] += x_push
				elif self.position[0] > self.gravity[0]:
					self.velocity[0] -= x_push
			else:
				x_push = None
			if difference[0] != 0:
				y_push = Dictionary.gravity_pull * abs(difference[1] / difference[0])
				if y_push > Dictionary.gravity_pull:
					y_push = Dictionary.gravity_pull
				if self.position[1] < self.gravity[1]:
					self.velocity[1] += y_push
				elif self.position[1] > self.gravity[1]:
					self.velocity[1] -= y_push
			else:
				y_push = None

	def movement(self, mouse_x, mouse_y):
		if self.held == True:
			self.velocity[0] = mouse_x - self.position[0]
			self.position[0] = mouse_x
			self.velocity[1] = mouse_y - self.position[1]
			self.position[1] = mouse_y
		elif self.sling == True:
			self.velocity[0] = (mouse_x - self.position[0]) / 5
			self.velocity[1] = (mouse_y - self.position[1]) / 5
		else:
			self.gravity_check()
			self.gravity_movement()
			self.position[0] += self.velocity[0]
			self.velocity[0] *= Dictionary.friction
			self.position[1] += self.velocity[1]
			self.velocity[1] *= Dictionary.friction
	
	def wall_collision(self):
		if self.position[0] - self.radius <= 0:
			self.position[0] = self.radius
			self.velocity[0] *= -Dictionary.friction
		elif self.position[0] + self.radius >= SCREEN_WIDTH:
			self.position[0] = SCREEN_WIDTH - self.radius
			self.velocity[0] *= -Dictionary.friction
		if self.position[1] - self.radius <= 0:
			self.position[1] = self.radius
			self.velocity[1] *= -Dictionary.friction
		elif self.position[1] + self.radius >= SCREEN_HEIGHT:
			self.position[1] = SCREEN_HEIGHT - self.radius
			self.velocity[1] *= -Dictionary.friction
	
	def ball_collision(self, sphere):
		if self.check_ball_collision(sphere) == False:
			return
		difference = self.position - sphere.position
		distance = math.sqrt(difference[0]**2 + difference[1]**2)
		push_radius = self.radius + sphere.radius
		offset = 1 - distance / push_radius
		if self.held == True or self.sling == True or self.check_wall_collision() == True:
			sphere.position = sphere.position - difference * offset
		elif sphere.held == True or sphere.sling == True or sphere.check_wall_collision() == True:
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
			
			if selfdenominator != 0 and spheredenominator != 0:
				self.velocity = self.velocity - mass[0] * (selfnumerator / selfdenominator) * selfposition
				sphere.velocity = sphere.velocity - mass[1] * (spherenumerator / spheredenominator) * sphereposition
			else:
				self.position = numpy.array([random.randrange(round(self.radius), SCREEN_WIDTH), random.randrange(round(self.radius), SCREEN_HEIGHT)])
				while self.check_ball_collision == True:
					self.position = numpy.array([random.randrange(round(self.radius), SCREEN_WIDTH), random.randrange(round(self.radius), SCREEN_HEIGHT)])
				self.velocity = numpy.array([0.0, 0.0])




