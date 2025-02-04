# main.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
# If pygame is not installed: sudo apt install python3-pygame
# To run: python3 Idlegame/main.py
import pygame
from ball import *
from variables import *
from background import draw_text_background

def main():
	run = True
	creating = False
	deleting = False
	shift = False
	space = False
	tabbed = False
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if shift == False:
						grab_ball(True)
					else:
						pull_ball(True)
				if event.button == 3:
					if shift == False:
						sling_ball(True)
					else:
						push_ball(True)
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					grab_ball(False)
					pull_ball(False)
				if event.button == 3:
					sling_ball(False)
					push_ball(False)
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
				if event.key == pygame.K_r:
					dictionary.clear()
				if event.key == pygame.K_SPACE:
					direction_change(0)
					if space == False:
						space = True
					else:
						space = False
				if space == False:
					if event.key == pygame.K_w or event.key == pygame.K_UP:
						direction_change(1)
					if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
						direction_change(2)
					if event.key == pygame.K_s or event.key == pygame.K_DOWN:
						direction_change(3)
					if event.key == pygame.K_a or event.key == pygame.K_LEFT:
						direction_change(4)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RETURN:
					creating = False
				if event.key == pygame.K_BACKSPACE:
					deleting = False
			if event.type == pygame.QUIT:
				run = False
		if creating == True:
			create_ball()
		if deleting == True:
			if len(dictionary) > 0:
				delete_ball()
		screen.fill(Black)
		draw_text_background(tabbed, shift, space)
		draw_ball()
		pygame.display.set_caption(f'{clock.get_fps() :.1f}')
		pygame.display.update()
		delta_time = clock.tick(FPS)
	pygame.quit()
main()
