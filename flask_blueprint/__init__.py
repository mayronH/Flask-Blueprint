from flask import Flask

def init_app():
    """Inicialização da aplicação"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Acessando as rotas de uma blueprint
        from .home import routes
        # from .clients import routes
        # from products import routes

        # Registrando as rotas na aplicação
        app.register_blueprint(home.routes.home_blueprint)

        return app