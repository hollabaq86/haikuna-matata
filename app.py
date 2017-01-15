from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os
import text_file


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

haikuFile = open("haikus.txt")
haikus = haikuFile.readlines()

hashed_haikus = text_file.parseIntoProbabilityHash(haikus)
for sourcePair, count in hashed_haikus.items():
	text_file.createUnigram(sourcePair, count)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
