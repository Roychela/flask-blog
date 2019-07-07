from flask_bootstrap import Bootstrap
from flask import Flask

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
     #Registering authentication blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    return app
