from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import *

# class Unigram(db.Model):
# 	__tablename__ = "unigrams"
# 	id = db.Column(db.Integer, primary_key=True)
# 	word1 = db.Column('word1', db.String, nullable=False, index=True)
# 	word2 = db.Column('word2', db.String)
# 	count = db.Column('count', db.Integer, nullable = False)

# 	def __init__(self, word1, word2, count):
# 	    self.word1 = word1
# 	    self.word2 = word2
# 	    self.count = count

# 	def __repr__(self):
# 	    return '<id {}>'.format(self.id)


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
