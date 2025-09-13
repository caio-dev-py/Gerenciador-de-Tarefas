from flask import Flask
from flask_login import LoginManager
from src.app.models import db, Usuarios
from src.app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # configurando login manager
    lm = LoginManager()
    lm.login_view = "auth.login"
    lm.login_message = "Acesso negado, faça o login para acessar a página."
    lm.login_message_category = "warning"
    
    lm.init_app(app)
    
    @lm.user_loader
    def load_user(id):
        return Usuarios.query.get(int(id))

    # registrando as blueprints

    from src.app.routes.home import home_route
    from src.app.routes.auth import auth_route
    from src.app.routes.user import user_route
    
    app.register_blueprint(home_route)
    app.register_blueprint(auth_route)
    app.register_blueprint(user_route)
    
    return app