from app import db
import math

def favorUnigram(wordOne, wordTwo):
  from models import Unigram
  unigram = Unigram.query.filter(Unigram.word1 == wordOne, Unigram.word2 == wordTwo).first()
  unigram.count += math.floor(unigram.count * 1.2) #This number is arbitrary and can be changed, it's just a placeholder
  db.session.commit()#update entry here

def unfavorUnigram(wordOne, wordTwo):
  from models import Unigram
  unigram = Unigram.query.filter(Unigram.word1 == wordOne, Unigram.word2 == wordTwo).first()
  if unigram.count > 1:
    unigram.count -= math.floor(unigram.count * 0.75) # See above.
  db.session.commit()

def favorLine(line):
  lineArray = line.split(" ")
  for i in range(len(lineArray) - 1):
    favorUnigram(lineArray[i], lineArray[i + 1])

def unfavorLine(line):
  lineArray = line.split(" ")
  for i in range(len(lineArray) - 1):
    unfavorUnigram(lineArray[i], lineArray[i + 1])
