# defineball.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import math, random
from variables import *

dictionary = []
color_dictionary = []

class Circle:
	def __init__(self, color, x_place, y_place):
		self.color = color
		self.x = [x_place, 0]
		self.y = [y_place, 0]
		self.radius = SCREEN_HEIGHT / 16
		self.friction = 9
		self.held = False
		self.sling = False
	
	def movement(self, mouse_x, mouse_y):
		if self.held == True:
			self.x[1] = mouse_x - self.x[0]
			self.x[0] = mouse_x
			self.y[1] = mouse_y - self.y[0]
			self.y[0] = mouse_y
		elif self.sling == True:
			self.x[1] = (mouse_x - self.x[0]) / self.friction
			self.y[1] = (mouse_y - self.y[0]) / self.friction
		else:
			self.x[0] += self.x[1]
			self.x[1] *= self.friction / 10
			if -1 < self.x[1] < 1:
				self.x[1] = 0
			self.y[0] += self.y[1]
			self.y[1] *= self.friction / 10
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
			if math.sqrt(x_diff**2 + y_diff**2) > 1:
				distance = math.sqrt(x_diff**2 + y_diff**2)
			else:
				distance = 1

			if x_diff != 0 and y_diff != 0:

				y_push = None
				if x_diff != 0:
					x_change = [self.x[1] * (push_radius - abs(y_diff)) / push_radius * (push_radius / distance), sphere.x[1] * (push_radius - abs(y_diff)) / push_radius * (push_radius / distance)]
					y_push = [self.x[1] * (1 - (push_radius - abs(y_diff)) / push_radius), sphere.x[1] * (1 - (push_radius - abs(y_diff)) / push_radius)]

					self.x[1] = self.x[1] - x_change[0] + x_change[1]
					sphere.x[1] = sphere.x[1] + x_change[0] - x_change[1]
				
				x_push = None
				if y_diff != 0:
					y_change = [self.y[1] * (push_radius - abs(x_diff)) / push_radius * (push_radius / distance), sphere.y[1] * (push_radius - abs(x_diff)) / push_radius * (push_radius / distance)]
					x_push = [self.y[1] * (1 - (push_radius - abs(x_diff)) / push_radius), sphere.y[1] * (1 - (push_radius - abs(x_diff)) / push_radius)]

					self.y[1] = self.y[1] - y_change[0] + y_change[1]
					sphere.y[1] = sphere.y[1] + y_change[0] - y_change[1]

				if x_push != None:
					if y_diff < 0 and x_diff > 0 or y_diff > 0 and x_diff < 0:
						self.x[1] = self.x[1] + x_push[0] - x_push[1]
						sphere.x[1] = sphere.x[1] - x_push[0] + x_push[1]
					else:
						self.x[1] = self.x[1] - x_push[0] + x_push[1]
						sphere.x[1] = sphere.x[1] + x_push[0] - x_push[1]
				
				if y_push != None:
					if x_diff < 0 and y_diff > 0 or x_diff > 0 and y_diff < 0:
						self.y[1] = self.y[1] + y_push[0] - y_push[1]
						sphere.y[1] = sphere.y[1] - y_push[0] + y_push[1]
					else:
						self.y[1] = self.y[1] - y_push[0] + y_push[1]
						sphere.y[1] = sphere.y[1] + y_push[0] - y_push[1]

			else:
				change = random.choice([-push_radius, push_radius]) / 2
				self.x[0] += change
				sphere.x[0] -= change
				change = random.choice([-push_radius, push_radius]) / 2
				self.y[0] += change
				sphere.y[0] -= change

# Do not put count above 4 untill I fix this shit.
# The issue lies within the ball collision function.
def create_ball():
	mouse_x, mouse_y = pygame.mouse.get_pos()
	can_create = True
	for sphere in dictionary:
		if (math.sqrt((sphere.x[0] - mouse_x)**2 + (sphere.y[0] - mouse_y)**2) <= sphere.radius * 2):
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
		if (math.sqrt((sphere.x[0] - mouse_x)**2 + (sphere.y[0] - mouse_y)**2) <= sphere.radius):
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




