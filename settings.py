class Settings():
	# A class to store all the settings for Alien Invasion
	
	def __init__(self):
		# initialize the games static settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_limit = 3

		# Bullet settings
		self.bullet_width = 30
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 300

		# Alien settings
		self.fleet_drop_speed = 50
		
		# How quickly the game speeds up
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game"""
		self.ship_speed_factor = 10.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 10

		#fleet direction 1 is Right & -1 is Left
		self.fleet_direction = 1

		# scoring
		self.alien_points = 50

	def increase_speed(self):
		#increase speed settings & alien point values
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
