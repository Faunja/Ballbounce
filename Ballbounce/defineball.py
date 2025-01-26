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
		self.position = [x_place, y_place]
		self.velocity = [0, 0]
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
		collide = False
		push_radius = self.radius + sphere.radius
		if self.velocity[0] > self.radius * 2 or self.velocity[1] > self.radius * 2:
			if self.sling == False:
				x_motion = round(abs(self.velocity[0]) / self.radius)
				y_motion = round(abs(self.velocity[1]) / self.radius)
				for x_range in range(x_motion):
					x_diff = (self.position[0] + self.velocity[0] * (x_range / x_motion) - sphere.position[0])
					for y_range in range(y_motion):
						y_diff = (self.position[1] + self.velocity[1] * (y_range / y_motion) - sphere.position[1])
						if (math.sqrt(x_diff**2 + y_diff**2) <= push_radius):
							collide = True
							break
					if collide == True:
						break
		else:
			x_diff = (self.position[0] - sphere.position[0])
			y_diff = (self.position[1] - sphere.position[1])
			if (math.sqrt(x_diff**2 + y_diff**2) <= push_radius):
				collide = True

		if collide == True:
			selfvelocity = self.velocity
			self.velocity[0] += ((sphere.velocity[0] - self.velocity[0]) * (sphere.position[0] - self.position[0])) / abs(sphere.position[0] - self.position[0]) ** 2 * (sphere.position[0] - self.position[0])
			sphere.velocity[0] += ((selfvelocity[0] - sphere.velocity[0]) * (selfvelocity[0] - sphere.position[0])) / abs(selfvelocity[0] - sphere.position[0]) ** 2 * (selfvelocity[0] - sphere.position[0])
			self.velocity[1] += ((sphere.velocity[1] - self.velocity[1]) * (sphere.position[1] - self.position[1])) / abs(sphere.position[1] - self.position[1]) ** 2 * (sphere.position[1] - self.position[1])
			sphere.velocity[1] += ((selfvelocity[1] - sphere.velocity[1]) * (selfvelocity[1] - sphere.position[1])) / abs(selfvelocity[1] - sphere.position[1]) ** 2 * (selfvelocity[1] - sphere.position[1])

# Do not put count above 4 untill I fix this shit.
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




