class Config(object):
    DEBUG = False
    
class ProductionConfig(Config):

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):

    TESTING = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:admin@localhost/MP_DEV"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY='DEV'