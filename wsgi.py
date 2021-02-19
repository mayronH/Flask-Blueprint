"""Arquivo principal da aplicação"""
from flask_blueprint import init_app


app = init_app()

if __name__ == "__main__":
    app.run()