
class Config:
	DEBUG = False
	TESTING = False
	SECRET_KEY = "secret"

class Development(Config):
	DEBUG = True

class Production(Config):
	SECRET_KEY = "an actually secret key"
