class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    MONGO_URI = "mongodb://localhost:27017/ovic"
    MONGO_DATABASE = "ovic"
    BLOG_CODE = "TECH"
    IMPORT_PATH = "/var/technical_blog/"
    CUSTOM_STATIC_PATH = "/var/images/"
    MONGO_BLOG_TABLE = "technical"
    MONGO_GALLERY_TABLE = "gallery"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
