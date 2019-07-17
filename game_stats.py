class GameStats():
	#Track statistics for AI

	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		
		#Begin AI in an inactive state
		self.game_active = False

		#High score - don't reset it
		self.high_score = 0


	def reset_stats(self):
		#Initialize stats that can change during the game
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1