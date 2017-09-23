from flask import Flask

# extension
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail



# db      = SQLAlchemy(app)
# migrate = Migrate(app, db)
# mail    = Mail(app)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)


mail = Mail()
db = SQLAlchemy()


def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  mail.init_app(app)
  db.init_app(app)

  from main import main
  app.registr_blueprint(main)

  return app

  