from app import db
#BEGIN Holly model file
#I pulled these commands from a tutorial, I don't think we need them if the db is initizlied in the app file
#from sqlalchemy import create_engine, Column, Integer, String, DateTime
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.engine.url import URL

# import settings (whatever file has our db credentials we should update this line)

#DeclarativeBase = declarative_base()

#def db_connect:
#	return create_engine(URL(**settings.DATABASE))

#def create_unigrams_table(engine):
#	DeclarativeBase.metadata.create_all(engine)

class Unigrams(db.Model):
	__tablename__ = "unigrams"

	id = db.Column(db.Integer, primary_key=True)
	word1 = db.Column('word1', db.String, nullable=False, index=True)
	word2 = db.Column('word2', db.String)
	count = db.Column('count', db.Integer, nullable = False)
  
#BEGIN Dennis's model file  
#from app import db
#not sure if we need the JSON dialect from postgres
#from sqlalchemy.dialects.postgresql import JSON

#this was the exampe from Dennis' tutorial. I modified my model for unigrams based on this syntax so I don't think we need this part
# class Result(db.Model):
#     __tablename__ = 'results'

#     id = db.Column(db.Integer, primary_key=True)
#     url = db.Column(db.String())
#     result_all = db.Column(JSON)
#     result_no_stop_words = db.Column(JSON)

#I modified the initialize method to fit our unigram model, I think we should keep these two methods

    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        self.count = 1

    def __repr__(self):
        return '<id {}>'.format(self.id)

