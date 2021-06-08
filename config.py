class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    MONGO_URI = "mongodb://localhost:27017/ovic"
    DATABASE = "ovic"
    BLOG = "technical_blog"
    IMPORT_PATH = "/var/technical_blog/"
    CUSTOM_STATIC_PATH = "/var/images/"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
