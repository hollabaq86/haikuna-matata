from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# from models import Unigrams


# @app.route('/')
# def hello():
#     return "Hello World!"


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)


# if __name__ == '__main__':
#     app.run()

from flask import render_template

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
