from flask import Flask
from config import config

# extension
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager


mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()

# при данном значении Flask-Login будет следить за IP-адресом 
# клиента и агентом браузера и завершать сеанс принудительно 
# при обнаружении изменений
login_manager.session_protection = 'strong'

# присваиваится имя канечной точки, соответствующей станице 
# аутентификации. Так ка маршрут login находится внутри 
# макета в его начало добавленно имя макета
login_manager.login_view = 'auth.login'


def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  mail.init_app(app)
  db.init_app(app)
  login_manager.init_app(app)

  from .main import main
  app.register_blueprint(main)
  from .auth import auth
  app.register_blueprint(auth)

  return app



