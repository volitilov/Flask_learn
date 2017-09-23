import os

basedir = os.path.abspath(os.path.dirname(__file__))


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
  
  # включение / отключение CSRF
  CSRF_ENABLED = True

  # папка, где храняться файлы SQLAlchemy-migrate
  SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
  # отслеживет изменение объектов и испускает сигналы
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  FLASKY_MAIL_SENDER = 'Admin volitilov@gmail.com'
  FLASKY_MAIL_SUBJECT_PREFIX = '[ Pythman ] '
  FLASKY_ADMIN = 'volitilov@gmail.com'

  @staticmethod
  def init_app(app):
    pass

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class DevelopmentConfug(Config):
  # включение / отключение отладчика
  DEBUG = True

  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 465
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  MAIL_USE_SSL = True
  MAIL_DEFAULT_SENDER = MAIL_USERNAME

  # путь к файлу к базе данных.
  SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'dev-data.sqlite')


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class TestingConfig(Config):
  TESTING = True

  # путь к файлу к базе данных.
  SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \      
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')




config = {
  'development': DevelopmentConfug,
  'testing': TestingConfig,
  'production': ProductionConfig,

  'default': DevelopmentConfug
}