# defineball.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import math, random
from variables import *

class Circle:
	def __init__(self, color):
		self.x = [SCREEN_WIDTH/2, 0]
		self.y = [SCREEN_HEIGHT/2, 0]
		self.held = False
		self.radius = SCREEN_HEIGHT/16
		self.color = color
	
	def movement(self, mouse_x, mouse_y):
		if self.held == False:
			self.x[0] += self.x[1]
			self.x[1] *= .9
			if -1 < self.x[1] < 1:
				self.x[1] = 0
			self.y[0] += self.y[1]
			self.y[1] *= .9
			if -1 < self.y[1] < 1:
				self.y[1] = 0
		else:
			self.x[1] = mouse_x - self.x[0]
			self.x[0] = mouse_x
			self.y[1] = mouse_y - self.y[0]
			self.y[0] = mouse_y
	
	def collision(self):
		if self.x[0] - self.radius <= 0:
			self.x[0] = self.radius
			self.x[1] *= -1
		elif self.x[0] + self.radius >= SCREEN_WIDTH:
			self.x[0] = SCREEN_WIDTH - self.radius
			self.x[1] *= -1
		if self.y[0] - self.radius <= 0:
			self.y[0] = self.radius
			self.y[1] *= -1
		elif self.y[0] + self.radius >= SCREEN_HEIGHT:
			self.y[0] = SCREEN_HEIGHT - self.radius
			self.y[1] *= -1
	
	def ball_collision(self, sphere):
		x_diff = (self.x[0] - sphere.x[0])
		y_diff = (self.y[0] - sphere.y[0])
		push_radius = self.radius + sphere.radius
		
		if (math.sqrt(x_diff**2 + y_diff**2) <= push_radius):
			distance = push_radius - math.sqrt(x_diff**2 + y_diff**2)
			if x_diff < 0:
				self.x[0] -= distance
				self.x[1] -= distance 
				sphere.x[1] += distance
			elif x_diff > 0:
				self.x[0] += distance
				self.x[1] += distance
				sphere.x[1] -= distance
			else:
				change = random.choice([-distance, distance]) / 2
				self.x[0] += change
				sphere.x[0] -= change
			if y_diff < 0:
				self.y[0] -= distance
				self.y[1] -= distance
				sphere.y[1] += distance
			elif y_diff > 0:
				self.y[0] += distance
				self.y[1] += distance
				sphere.y[1] -= distance
			else:
				change = random.choice([-distance, distance]) / 2
				self.y[0] += change
				sphere.y[0] -= change
