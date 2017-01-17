from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import os
# import run_text_files
	

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import *

@app.route('/')
def index():
  return render_template('hello.html')

@app.route('/hello')
def hello():
  return render_template('hello.html')

@app.route('/haiku', methods=['POST'])
def haiku():
  word = request.form['word']
  processed_word = word.lower()
  from runner import generateHaiku
  result = generateHaiku(processed_word).split('\n')
  return render_template('show.html', word=processed_word, result=result)

if __name__ == '__main__':
  app.run()
