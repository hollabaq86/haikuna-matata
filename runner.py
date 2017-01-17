import nltk
from nltk.corpus import cmudict
import curses
from curses.ascii import isdigit
import re
from nltk.probability import FreqDist
from app import db
import models
from random import randrange

d = cmudict.dict()

def numSylsInWord(word):
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
    syllableCount += numSylsInWord(i)
  return syllableCount

def generateHaiku(firstWord):
  haiku = ""
  haiku += generateRandomLine(5, firstWord)
  haiku += "\n"
  haiku += generateRandomLine(7)
  haiku += "\n"
  haiku += generateRandomLine(5)
  return haiku

def generateRandomLine(sylCount, startingWord= None):
  if not startingWord:
    startingWord = pickRandomWord(sylCount)
  remainingSylCount = sylCount - countSyllables(startingWord)
  line = buildLine(remainingSylCount, [startingWord])
  return " ".join(line)

def buildLineList(sylCount, wordsFromBefore):
  if sylCount == 0:
    return wordsFromBefore
  lastWord = wordsFromBefore[-1]
  possibilities = grabPossibleWords(lastWord, sylCount) 
  for possibileWord in possibilities:
    newWordsFromBefore = [word[:] for word in wordsFromBefore]
    newWordsFromBefore.append(possibileWord) 
    newSyllableCount = sylCount - countSyllables(possibleWord)
    result = buildLineList(newSyllableCount, newWordsFromBefore)
    if not result:
      return result
  return None  

  # if sylCount == 0:
  #   return wordsFromBefore
  # elif sylCount < 0:
  #   return "You fucked up"
  # if wordsFromBefore == None:
  #   wordsFromBefore = pickRandomWord(sylCount)
  # lastWord = wordsFromBefore.rsplit(None, 1)[-1]
  # possibleWords = grabPossibleWords(lastWord, sylCount)
  # if possibleWords:
  #   index = randrange(0, len(possibleWords))
  #   adder = possibleWords[index]
  # if not possibleWords:
  #   adder = pickRandomWord(sylCount)
  # newwordsFromBefore = wordsFromBefore + " " + adder
  # workingSylCount = sylCount - countSyllables(adder)
  # return generateLine(workingSylCount, newBase)

def pickRandomWord(reqSylCount):
  from models import Unigram
  lengthDB = Unigram.query.count()
  while True:
    randomNumPick = randrange(0, lengthDB)
    tryWord = Unigram.query.filter(Unigram.id == randomNumPick).first()
    if countSyllables(tryWord.word1) <= reqSylCount:
      word = tryWord.word1
      break
  return word  

def formatPossibleWords(unigrams, reqSylCount):
  container = []
  for each in unigrams:
      for unigram in range(each.count):
          if countSyllables(each.word2) <= reqSylCount:
            container.append(each.word2)
  return container

def grabPossibleWords(baseWord, reqSylCount):
  from models import Unigram
  listOfUnigrams = Unigram.query.filter(Unigram.word1 ==baseWord)
  return formatPossibleWords(listOfUnigrams, reqSylCount)     

# def identifyPartsOfSpeech(string):
#   cleanString = re.sub(ur"[^\w\d'\s]+",' ', string)
#   arrayOfWords = nltk.word_tokenize(cleanString)

#   return nltk.pos_tag(arrayOfWords)

# def findFrequency(largeBodyofText):
#   cleanText = re.sub(ur"[^\w\d'\s]+",' ', largeBodyofText)
#   arrayOfWords = nltk.word_tokenize(cleanText)
#   fdist = FreqDist(arrayOfWords)
#   uniqueWords = []
#   for word in arrayOfWords:
#     if not word in uniqueWords:
#       uniqueWords.append(word)
#   for word in uniqueWords:
#     print(word, fdist[word])


print(generateHaiku("the"))

# index of the parts of speech tags outputted by identifyingPartsOfSpeech() method
# http://www.scs.leeds.ac.uk/amalgam/tagsets/brown.html


