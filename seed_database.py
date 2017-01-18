from flask_sqlalchemy import SQLAlchemy
import re
from models import *
import nltk
from nltk.corpus import cmudict
import curses
from curses.ascii import isdigit
d = cmudict.dict()

#tests will only pass if you move this declaration of the empty probability hash to inside of the parse method
probabilityHash = {}

def parseIntoProbabilityHash(text):
  stripPunctuation = ""
  for line in text:
    stripPunctuationLine = re.sub(ur"[^\w\d'\s]+",'',line)
    # stripPunctuationLine = re.sub("\b([a-zA-Z]+)\b",' ',line)
    stripPunctuation += stripPunctuationLine
  wordsInText = stripPunctuation.split()
  i = 0
  count = len(wordsInText) - 1
  while (i < count):
    word1 = wordsInText[i].lower()
    word2 = wordsInText[i+1].lower()
    if word1 in d and word2 in d:
      if (word1 + " " + word2) in probabilityHash:
        probabilityHash[word1 + " " + word2] += 1
      else:
        probabilityHash[word1 + " " + word2] = 1
    i+=1
  return probabilityHash

def createUnigram(unigramSourcePair, count):
  split_text = unigramSourcePair.split(" ")
  new_unigram = Unigram(word1 = split_text[0], word2 = split_text[1], count = count)
  db.session.add(new_unigram)
  db.session.commit()


#runner logic
files = ['example_poetry/sample1.txt', 'example_poetry/sample2.txt', 'example_poetry/sample3.txt', 'example_poetry/sample4.txt', 'example_poetry/sample5.txt', 'example_poetry/sample6.txt', 'example_poetry/sample7.txt', 'example_poetry/adelle.txt']
testFiles = ['example_poetry/test_text.txt']
# files variable passed in must be an array.  If only passing in one file, still must be an array.
herokuTest = ['example_poetry/sample2.txt']
def seedDatabase(files):
  for txtfile in files:
    haikuFile = open(txtfile)
    haikus = haikuFile.readlines()
    hashed_haikus = parseIntoProbabilityHash(haikus)
    print("processing")
  for sourcePair, count in hashed_haikus.items():
    createUnigram(sourcePair, count)

seedDatabase(files)
#seedDatabase(herokuTest)

