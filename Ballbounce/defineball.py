# defineball.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import math, random
from variables import *

dictionary = []
color_dictionary = []

class Circle:
	def __init__(self, color):
		self.color = color
		self.x = [SCREEN_WIDTH / 2, 0]
		self.y = [SCREEN_HEIGHT / 2, 0]
		self.radius = SCREEN_HEIGHT / 16
		self.held = False
		self.sling = False
	
	def movement(self, mouse_x, mouse_y):
		if self.held == True:
			self.x[1] = mouse_x - self.x[0]
			self.x[0] = mouse_x
			self.y[1] = mouse_y - self.y[0]
			self.y[0] = mouse_y
		elif self.sling == True:
			self.x[1] = mouse_x - self.x[0]
			self.y[1] = mouse_y - self.y[0]
		else:
			self.x[0] += self.x[1]
			self.x[1] *= .9
			if -1 < self.x[1] < 1:
				self.x[1] = 0
			self.y[0] += self.y[1]
			self.y[1] *= .9
			if -1 < self.y[1] < 1:
				self.y[1] = 0
	
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
		collide = False
		push_radius = self.radius + sphere.radius
		if self.x[1] > self.radius * 2 or self.y[1] > self.radius * 2:
			if self.sling == False:
				x_motion = round(abs(self.x[1]) / self.radius)
				y_motion = round(abs(self.y[1]) / self.radius)
				for x_range in range(x_motion):
					x_diff = (self.x[0] + self.x[1] * (x_range / x_motion) - sphere.x[0])
					for y_range in range(y_motion):
						y_diff = (self.y[0] + self.y[1] * (y_range / y_motion) - sphere.y[0])
						if (math.sqrt(x_diff**2 + y_diff**2) <= push_radius):
							collide = True
							break
					if collide == True:
						break
		else:
			x_diff = (self.x[0] - sphere.x[0])
			y_diff = (self.y[0] - sphere.y[0])
			if (math.sqrt(x_diff**2 + y_diff**2) <= push_radius):
				collide = True
		if collide == True:
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

# Do not put count above 16 untill I fix this shit.
# The issue lies within the ball collision function.
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
	for cylinder in dictionary:
		if cylinder.color != sphere.color:
			sphere.ball_collision(cylinder)
	sphere.movement(mouse_x, mouse_y)
	sphere.collision()
