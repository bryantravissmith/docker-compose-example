SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'rootpass'
DATABASE_NAME = 'counter'
DB_HOST = 'postgresql'
DB_URI = 'postgresql+psycopg2://%s:%s@%s/%s' \
    % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
