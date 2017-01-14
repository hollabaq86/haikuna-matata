from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

# import settings (whatever file has our db credentials we should update this line)

DeclarativeBase = declarative_base()

def db_connect:
	return create_engine(URL(**settings.DATABASE))

def create_unigrams_table(engine):
	DeclarativeBase.metadata.create_all(engine)

class Unigrams(DeclarativeBase):
	__tablename__ = "unigrams"

	id = Column(Integer, primary_key=True)
	word1 = Column('word1', String, nullable=False, index=True)
	word2 = Column('word2', String)
	count = Column('count', Integer, nullable = False)