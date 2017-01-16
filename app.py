from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os
import text_file

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# class Unigram(db.Model):
# 	__tablename__ = "unigrams"

# 	id = db.Column(db.Integer, primary_key=True)
# 	word1 = db.Column('word1', db.String, nullable=False, index=True)
# 	word2 = db.Column('word2', db.String)
# 	count = db.Column('count', db.Integer, nullable = False)

# def __init__(self, word1, word2, count):
#     self.word1 = word1
#     self.word2 = word2
#     self.count = count


# def __repr__(self):
#     return '<id {}>'.format(self.id)
    
def createUnigram(unigramSourcePair, count):
	split_text = unigramSourcePair.split(" ")
	new_unigram = Unigram(word1 = split_text[0], word2 = split_text[1], count = count)
	db.session.add(new_unigram)
	db.session.commit()

@app.route('/parse')
def parse():
	haikuFile = open("haikus.txt")
	haikus = haikuFile.readlines()
	hashed_haikus = text_file.parseIntoProbabilityHash(haikus)
	for sourcePair, count in hashed_haikus.items():
		createUnigram(sourcePair, count)
	return hashed_haikus


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
