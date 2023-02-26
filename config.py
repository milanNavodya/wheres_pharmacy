from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)  # create instance of flask
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/wheres_pharmacy'
    # Connect to the database
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'routes.index'
    login_manager.init_app(app)

    from routes import route_obj as routes_blueprint
    app.register_blueprint(routes_blueprint)
    # blueprint for non-auth parts of app
    from app import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    return app

