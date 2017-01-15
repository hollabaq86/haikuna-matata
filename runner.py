import nltk
from nltk.corpus import cmudict
import curses
from curses.ascii import isdigit
# import string
import re
from random import randrange
from nltk.probability import FreqDist
# from nltk.corpus import brown

d = cmudict.dict()

# this method ONLY works on words that are in the dict();
# need to tweak it
def numSylsInWord(word):
  if word.lower() in d:
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
  # else:
    #create "Contains an unrecognized word" error


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
  haiku += generateLine(5, firstWord)
  haiku += "\n"
  haiku += generateLine(7)
  haiku += "\n"
  haiku += generateLine(5)
  return haiku


def generateLine(sylCount, base= None):
  if sylCount == 0:
    return base
  elif sylCount < 0:
    return "You fucked up"
  if base == None:
    base = "The"
  lastWord = base.rsplit(None, 1)[-1]
  unigrams = session.query(Unigrams).filter_by(word1 == lastWord)
  possibleWords = grabPossibleWords(unigrams)
  index = randrange(0, len(possibleWords))
  adder = possibleWords[index]
  #we think we're getting infinitly stuck in this while loop. to be determined once we can test with this database
  while countSyllables(adder) > sylCount:
    index = randrange(0, len(possibleWords))
    adder = possibleWords[index]
  newBase = base + " " + adder
  newSylCount = sylCount - countSyllables(adder)
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



print(identifyPartsOfSpeech("isn't this orange juice yummy! I sure think it is."))


raw = "i love python. it's a lot of fun learning to break language apart using the national language toolkit. python is pretty cool. i am pretty tired though. i can't wait for it to be bedtime"

findFrequency(raw)


# index of the parts of speech tags outputted by identifyingPartsOfSpeech() method
# http://www.scs.leeds.ac.uk/amalgam/tagsets/brown.html




