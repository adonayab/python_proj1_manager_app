class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bzmanager:bzmanager@localhost:3306/bzmanager'
    SQLALCHEMY_ECHO = False  # Will not echo querying in terminal
