# main.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
# If pygame is not installed: sudo apt install python3-pygame
# To run: python3 Idlegame/main.py
import pygame
from background import draw_ball_background
from ball import *
from variables import *

def main():
	run = True
	
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					grab_ball(True)
				if event.button == 3:
					sling_ball(True)
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					grab_ball(False)
				if event.button == 3:
					sling_ball(False)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
				if event.key == pygame.K_RETURN:
					if len(dictionary) < 20:
						create_ball()
				if event.key == pygame.K_BACKSPACE:
					if len(dictionary) > 0:
						delete_ball()
				if event.key == pygame.K_s:
					stop_ball()
				if event.key == pygame.K_r:
					random_ball()
			if event.type == pygame.QUIT:
				run = False
		draw_ball_background()
		draw_ball()
		delta_time = clock.tick(FPS)
		pygame.display.set_caption(f'{clock.get_fps() :.1f}')
		pygame.display.update()
	pygame.quit()
main()
