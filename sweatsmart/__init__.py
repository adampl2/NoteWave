import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
if os.path.exists("env.py"):
    import env  # noqa


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sweatsmart_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .routes import routes
    from .auth import auth

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('sweatsmart/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')