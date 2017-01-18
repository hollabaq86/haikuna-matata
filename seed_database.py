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

def scrubText(text, punctuation):
  separatedLines = [line.split(punctuation) for line in text]
  separatedLines = [string for sublist in separatedLines for string in sublist]
  separatedLines = filter(None, separatedLines)
  return separatedLines

def parseIntoProbabilityHash(text, existingHash):
  stripPunctuationFailsafe = [re.sub(ur"[^\w\d'\s]+",'',string) for string in text]
  sectionsToParse = [string.split() for string in text]
  masterHash = existingHash
  masterHash = [build_hash(masterHash, section) for section in sectionsToParse][0]
  return masterHash


def build_hash(existingHash, listToFormat):
  i = 0
  count = len(listToFormat) - 1
  while (i < count):
    twoWordString = listToFormat[i].lower() + " " + listToFormat[i+1].lower()
    format_hash(existingHash, twoWordString)
    i += 1
  return existingHash

def format_hash(existingHash, twoWordString):
  if twoWordString in existingHash:
    existingHash[twoWordString] += 1
  else:
    existingHash[twoWordString] = 1
  return existingHash        

def createUnigram(unigramSourcePair, count):
  split_text = unigramSourcePair.split(" ")
  new_unigram = Unigram(word1 = split_text[0], word2 = split_text[1], count = count)
  db.session.add(new_unigram)
  db.session.commit()


#runner logic
files = ['example_poetry/sample1.txt', 'example_poetry/sample2.txt', 'example_poetry/sample3.txt', 'example_poetry/sample4.txt', 'example_poetry/sample5.txt', 'example_poetry/sample6.txt']
# files = ["example_poetry/fix_parser.txt", "example_poetry/fix_parser.txt"]
testFiles = ['example_poetry/test_text.txt']
# files variable passed in must be an array.  If only passing in one file, still must be an array.
def seedDatabase(files):
  hashed_haikus = {}  
  for txtfile in files:
    haikuFile = open(txtfile)
    haikus = haikuFile.readlines()
    haikus = [string.replace("\n", "") for string in haikus]
    punctuationList = [".", "?", "!", ":", ";", "(", ")"]
    for punctuation in punctuationList:
      haikus = scrubText(haikus, punctuation)
    hashed_haikus = parseIntoProbabilityHash(haikus, hashed_haikus)  
    print "****processing... current hash****"
    print hashed_haikus
    print "***********************************"
  # for sourcePair, count in hashed_haikus.items():
  #   createUnigram(sourcePair, count)

seedDatabase(files)