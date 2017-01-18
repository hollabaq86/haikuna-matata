from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import os


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
  if request.is_xhr:
    word = request.form['word']
    processed_word = word.lower()
    from runner import generateHaiku
    result = generateHaiku(processed_word).split('\n')
    line1 = result[0]
    line2 = result[1]
    line3 = result[2]
    return jsonify(lineOne=line1, lineTwo=line2, lineThree=line3)
  else:
    word = request.form['word']
    processed_word = word.lower()
    from runner import generateHaiku
    result = generateHaiku(processed_word).split('\n')
    return render_template('show.html', word=processed_word, result=result)

@app.route('/train', methods=['POST'])
def train():
  update = request.form['update']
  from training import favorUnigram, unfavorUnigram, favorLine, unfavorLine
  if update == "like1":
    favorLine(request.form['line1'])
  elif update == "like2":
    favorLine(request.form['line2'])
  elif update == "like3":
    favorLine(request.form['line3'])
  elif update == "dislike1":
    unfavorLine(request.form['line1'])
  elif update == "dislike2":
    unfavorLine(request.form['line2'])
  else:
    unfavorLine(request.form['line2'])
  return render_template('hello.html')

if __name__ == '__main__':
  app.run()
