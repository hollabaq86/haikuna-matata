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
  if request.is_xhr:
    print(request)
    print("in xhr")
    update1 = request.args.get("update1", "null", type=basestring)
    update2 = request.args.get("update2", "null", type=basestring)
    update3 = request.args.get("update3", "null", type=basestring)
    print(update1)
    print(update2)
    print(update3)
    from training import favorUnigram, unfavorUnigram, favorLine, unfavorLine
    if update1 == "like1":
      print("you liked 1")
      favorLine(request.args.get("lineOne", "You Messed Up", type=basestring))
    elif update1 == "dislike1":
      print("you disliked 1")
      unfavorLine(request.args.get("lineOne", "You Messed Up", type=basestring))
    if update2 == "like2":
      print("you liked 2")
      favorLine(request.args.get("lineTwo", "You Messed Up", type=basestring))
    elif update2 == "dislike2":
      print("you disliked2")
      unfavorLine(request.args.get("lineTwo", "You Messed Up", type=basestring))
    if update3 == "like3":
      print("you liked 3")
      favorLine(request.args.get("lineThree", "You Messed Up", type=basestring))
    elif update3 == "dislike3":
      print("you disliked 3")
      unfavorLine(request.args.get("lineThree", "You Messed Up", type=basestring))
    return jsonify(result="thank you!")
  else:
    update1 = request.form['update1']
    update2 = request.form['update2']
    update3 = request.form['update3']
    from training import favorUnigram, unfavorUnigram, favorLine, unfavorLine
    if update1 == "like1":
      favorLine(request.form['line1'])
    elif update1 == "dislike1":
      unfavorLine(request.form['line1'])
    if update2 == "like2":
      favorLine(request.form['line2'])
    elif update2 == "dislike2":
      unfavorLine(request.form['line2'])
    if update3 == "like3":
      favorLine(request.form['line3'])
    elif update3 == dislike3:
      unfavorLine(request.form['line3'])
    return render_template('hello.html')

if __name__ == '__main__':
  app.run()
