"""
Algorithm for training the machine (note this file doesn't include the proper imports,
	will fix later):

	Bot should have 2 modes: Creation and Training
	Creation is the main poem-writing function of the bot
  	- Function will be as normal
  Training allows the user to inspect past poems and either 'like' or 'dislike'
  lines of the haiku that they don't like
  	If a line is disliked:
  		Each unigram that makes up the line will have it's count halved or decreased
  		by some value, so that the probability of those words occurring together again
  		decreases.
  	Likewise, if a line is liked:
  		Each unigram will have it's count increased by some factor to increase the chance
  		of that unigram occurring again.
  	If there is time, this method could be refined to target specific unigrams in the line,
  	as well as implementing a sort of rating system that'll increase/decrease the probability of
  	the unigram occurring so that the probability changes occur at different degrees.
"""

def favorUnigram(wordOne, wordTwo):
	unigram = session.query(Unigrams).filter_by(word1 == wordOne, word2 == wordTwo)
	Unigram.count = math.floor(Unigram.count * 1.5) #This number is arbitrary and can be changed, it's just a placeholder
	#update entry here

def unfavorUnigram(wordOne, wordTwo):
	unigram = session.query(Unigrams).filter_by(word1 == wordOne, word2 == wordTwo)
	Unigram.count = math.floor(Unigram.count * 0.5)
	#update entry here