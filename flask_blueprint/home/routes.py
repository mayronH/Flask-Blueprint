from flask import Blueprint
from flask.templating import render_template

# Modularizando a aplicação, cada Blueprint tem seu proprio diretorio de templates,statics e suas proprias rotas
home_blueprint = Blueprint(
    'home_blueprint', __name__, template_folder='templates', static_folder='static', static_url_path='/home/static/'
)

@home_blueprint.route('/', methods=['GET'])
def home():
    """Homepage view"""
    return render_template('index.html')