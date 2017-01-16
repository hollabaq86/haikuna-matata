from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os
import text_file

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
    return 'Index Page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
