class Settings():
	def __init__(self):
		self.bullet_wight = 10000
		self.bullet_height = 15
		self.bullet_color = ("Red")
		self.bullets_allowed = 3
		self.ship_speed = 194472374623542734652374
		self.ship_limit = 3
		self.screen_wight = 1375
		self.screen_height = 715
		self.bg_color = ("Black")
		self.alien_speed = 0.1
		self.fleet_drop_speed = 10
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()
		self.fleet_direction = 1
	def initialize_dynamic_settings(self):
		self.ship_speed = 3
		self.bullet_speed = 3.0
		self.alien_speed = 3.0
		self.fleet_direction = 1
		self.alien_points = 18125173612735126333424234234234234234234234234
	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)