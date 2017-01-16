import nltk
from nltk.corpus import cmudict
import curses
from curses.ascii import isdigit
# import run_text_files
# import string
import re
from random import randrange
from nltk.probability import FreqDist
from app import db
import models
# from nltk.corpus import brown

d = cmudict.dict()

def numSylsInWord(word):
  print(word)
  if word.lower() in d:
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]



def isHaiku(potentialHaiku):
  syllableCount = countSyllables(potentialHaiku)
  if syllableCount == 17:
    #how do we want to break this down?
    #what are the other "ifs" that this conditional needs to meet?
    result = True
  else:
    result = False

  return result


def countSyllables(potentialHaiku):
  stripPunctuation = re.sub(ur"[^\w\d'\s]+",' ',potentialHaiku)
  wordsInHaiku = stripPunctuation.split()
  syllableCount = 0
  for i in wordsInHaiku:
    # print"*** countSyllables method***"
    # print i
    # print"***"
    syllableCount += numSylsInWord(i)
  return syllableCount

def generateHaiku(firstWord):
  haiku = ""
  haiku += generateLine(4, firstWord)
  haiku += "\n"
  haiku += generateLine(6)
  haiku += "\n"
  haiku += generateLine(4)
  return haiku


def generateLine(sylCount, base= None):
  if sylCount == 0:
    return base
  elif sylCount < 0:
    return "You fucked up"
  if base == None:
    base = "the"
  lastWord = base.rsplit(None, 1)[-1]
  from models import Unigram
  listOfUnigrams = Unigram.query.filter(Unigram.word1 ==lastWord)
  possibleWords = grabPossibleWords(listOfUnigrams)
  index = randrange(0, len(possibleWords))
  adder = possibleWords[index]
  #we think we're getting infinitly stuck in this while loop. to be determined once we can test with this database
  while countSyllables(adder) > sylCount:
    index = randrange(0, len(possibleWords))
    adder = possibleWords[index]
  newBase = base + " " + adder
  newSylCount = sylCount - countSyllables(adder)
  print newBase
  return generateLine(newSylCount, newBase)

def grabPossibleWords(unigrams):
  container = []
  for each in unigrams:
      for unigram in range(each.count):
        container.append(each.word2)
  return container

def identifyPartsOfSpeech(string):
  cleanString = re.sub(ur"[^\w\d'\s]+",' ', string)
  arrayOfWords = nltk.word_tokenize(cleanString)

  return nltk.pos_tag(arrayOfWords)

def findFrequency(largeBodyofText):
  cleanText = re.sub(ur"[^\w\d'\s]+",' ', largeBodyofText)
  arrayOfWords = nltk.word_tokenize(cleanText)
  fdist = FreqDist(arrayOfWords)
  uniqueWords = []
  for word in arrayOfWords:
    if not word in uniqueWords:
      uniqueWords.append(word)
  for word in uniqueWords:
    print(word, fdist[word])

print(generateHaiku("give"))
# index of the parts of speech tags outputted by identifyingPartsOfSpeech() method
# http://www.scs.leeds.ac.uk/amalgam/tagsets/brown.html

print generateHaiku("the")


