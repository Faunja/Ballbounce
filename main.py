# main.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
# If pygame is not installed: sudo apt install python3-pygame
# To run: python3 Ballbounce/main.py
import pygame
from ball import *
from variables import *
from background import draw_text_background

def main():
	run = True
	creating = False
	deleting = False
	culling = False
	time_since_cull = 0
	shift = False
	tabbed = False
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if shift == False:
						grab_ball(True)
					else:
						Dictionary.pulled = True
				if event.button == 3:
					if shift == False:
						sling_ball(True)
					else:
						Dictionary.pushed = True
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					grab_ball(False)
					Dictionary.pulled = False
				if event.button == 3:
					sling_ball(False)
					Dictionary.pushed = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
				if event.key == pygame.K_TAB:
					if tabbed == False:
						tabbed = True
					else:
						tabbed = False
				if event.key == pygame.K_RETURN:
					creating = True
				if event.key == pygame.K_BACKSPACE:
					deleting = True
				if event.key == pygame.K_LSHIFT:
					if shift == False:
						shift = True
					else:
						shift = False
				if event.key == pygame.K_c:
					if Dictionary.collision == True:
						Dictionary.collision = False
					else:
						Dictionary.collision = True
				if event.key == pygame.K_f:
					if Dictionary.friction != 1:
						Dictionary.friction = 1
					else:
						Dictionary.friction = .9
				if event.key == pygame.K_r:
					Dictionary.dictionary.clear()
				if event.key == pygame.K_g:
					for sphere in Dictionary.dictionary:
						if sphere.held == True:
							if sphere.pull == False and sphere.push == False:
								sphere.pull = True
							elif sphere.push == True:
								sphere.push = False
							elif sphere.pull == True:
								sphere.pull = False
				if event.key == pygame.K_SPACE:
					if Dictionary.space == False:
						Dictionary.space = True
					else:
						Dictionary.space = False
				if Dictionary.space == False:
					if event.key == pygame.K_w or event.key == pygame.K_UP:
						Dictionary.direction = 1
					if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
						Dictionary.direction = 2
					if event.key == pygame.K_s or event.key == pygame.K_DOWN:
						Dictionary.direction = 3
					if event.key == pygame.K_a or event.key == pygame.K_LEFT:
						Dictionary.direction = 4
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RETURN:
					creating = False
				if event.key == pygame.K_BACKSPACE:
					deleting = False
			if event.type == pygame.QUIT:
				run = False
		if culling == False:
			if creating == True:
				if float(f'{clock.get_fps() :.1f}') > 45:
					Dictionary.create_ball()
			if float(f'{clock.get_fps() :.1f}') <= 30 and len(Dictionary.dictionary) != 0:
				culling = True
		else:
			if float(f'{clock.get_fps() :.1f}') < 50 and len(Dictionary.dictionary) != 0:
				time_since_cull += 1
				if time_since_cull == 1:
					Dictionary.delete_ball(True)
				elif time_since_cull == round(FPS / 4):
					time_since_cull = 0
			else:
				culling = False
				time_since_cull = 0
		if deleting == True:
			if len(Dictionary.dictionary) > 0:
				Dictionary.delete_ball()
		screen.fill(Black)
		draw_text_background(tabbed, shift, Dictionary.space, Dictionary.friction, Dictionary.collision)
		draw_ball()
		pygame.display.set_caption(f'{clock.get_fps() :.1f}')
		pygame.display.update()
		delta_time = clock.tick(FPS)
	pygame.quit()
main()
