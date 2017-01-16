from app import db

class Unigram(db.Model):
	__tablename__ = "unigrams"
	__table_args__ = {'extend_existing': True}

	id = db.Column(db.Integer, primary_key=True)
	word1 = db.Column('word1', db.String, nullable=False, index=True)
	word2 = db.Column('word2', db.String)
	count = db.Column('count', db.Integer, nullable = False)

	def __init__(self, word1, word2, count):
		self.word1 = word1
		self.word2 = word2
		self.count = count

	def __repr__(self):
		return '<id {}>'.format(self.id)

