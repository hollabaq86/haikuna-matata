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

@app.route('/train', methods=['POST'])
def train():
  update = request.form['update']
  if update == "like1":
    favorUnigram(request.form['line1'])
  elif update == "like2":
    favorUnigram(request.form['line2'])
  elif update == "like3":
    favorUnigram(request.form['line3'])
  elif update == "dislike1":
    unfavorUnigram(request.form['line1'])
  elif update == "dislike2":
    unfavorUnigram(request.form['line2'])
  else:
    unfavorUnigram(request.form['line2'])
  return render_template('hello.html')

if __name__ == '__main__':
  app.run()
