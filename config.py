from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)  # create instance of flask
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://openpg:openpgpwd@localhost/pharmacy'
    # Connect to the database
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'routes.index'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)
    # blueprint for non-auth parts of app
    from app import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    return app

