from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '60ef47dfe22df53aa7d3fc4e9ee39c0c'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'

db = SQLAlchemy(app)


from climb import routes 