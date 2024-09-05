from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ba79b37d00047525a5e833980f864e91'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///projeto.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#Redireciona as telas necessárias de login pra tela de login
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'
#Fica em baixo pois o init precisa chamar as rotas
from projcontrole import routes