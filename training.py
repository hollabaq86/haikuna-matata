"""
 +Algorithm for training the machine (note this file doesn't include the proper imports,
 +  will fix later):
 +
 +  Bot should have 2 modes: Creation and Training
 +  Creation is the main poem-writing function of the bot
 +    - Function will be as normal
 +  Training allows the user to inspect past poems and either 'like' or 'dislike'
 +  lines of the haiku that they don't like
 +    If a line is disliked:
 +      Each unigram that makes up the line will have it's count halved or decreased
 +      by some value, so that the probability of those words occurring together again
 +      decreases.
 +    Likewise, if a line is liked:
 +      Each unigram will have it's count increased by some factor to increase the chance
 +      of that unigram occurring again.
 +    If there is time, this method could be refined to target specific unigrams in the line,
 +    as well as implementing a sort of rating system that'll increase/decrease the probability of
 +    the unigram occurring so that the probability changes occur at different degrees.
 +"""
 import models


 def favorUnigram(wordOne, wordTwo):
   unigram = Unigram.query.filter_by(Unigram.word1 == wordOne, Unigram.word2 == wordTwo)
   unigram.count += math.floor(unigram.count * 1.2)
   db.session.commit()


 def unfavorUnigram(wordOne, wordTwo):
   unigram = session.query(Unigrams).filter_by(word1 == wordOne, word2 == wordTwo)
   if unigram.count > 1:
    unigram.count -= math.floor(unigram.count * 0.75) # See above.
   db.session.commit()

 def favorLine(line):
  lineList = line.split(' ')
    for i in len(lineList) - 1:
      favorUnigram(lineList[i], lineList[i + 1])


 def unfavorLine(line):
  lineList = line.split(' ')
  for i in len(lineList) - 1:
    unfavorUnigram(lineList[i], lineList[i + 1])
