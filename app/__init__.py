from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Criando uma instância do aplicativo Flask:
app = Flask(__name__)

# Configurando o aplicativo Flask a partir do arquivo de configuração
app.config.from_object('config')

# Configurando um banco de dados com SQLAlchemy
# cria uma instância do SQLAlchemy associada ao aplicativo Flask "app"
db = SQLAlchemy(app)

# Configurando migrações de banco de dados com Flask-Migrate
# migrate recebe o banco de dados e a aplicação para poder cuidar das migrações
migrate = Migrate(app, db)

# Configurando o gerenciador de login com Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Importando módulos e pacotes relacionados ao aplicativo
from app.models import tables, forms #Importa as tabelas e os formulários
from app.controllers import default #Importa as rotas


