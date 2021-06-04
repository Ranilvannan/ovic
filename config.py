class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/ovic?user=ramesh&password=ramesh"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CUSTOM_STATIC_PATH = "/var/images/"
    ASSETS_PATH = "/var/images/"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
