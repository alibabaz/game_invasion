import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button

def run_game():
	# initialize pygame, settings and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#make the play button
	play_button = Button(ai_settings, screen, "Play")

	#create an instance to store game stats & create a scoreboard
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# Make the ship, group of bullets & group of aliens
	ship = Ship(ai_settings, screen)
	aliens = Group()
	bullets = Group()

	# Create the fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# The main loop for game
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, 
						ship, aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, 
								aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
							bullets, play_button)

run_game()