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

def inDatabase(firstWord):
	container = []
	from models import Unigram
	unigrams = Unigram.query.filter(Unigram.word1 == firstWord)
	for each in unigrams:
			for unigram in range(each.count):
					container.append(each.word2)
	if not container:
		return False
	if container:
		return True



def inDatabase(firstWord):
  container = []
  from models import Unigram
  unigrams = Unigram.query.filter(Unigram.word1 == firstWord)
  for each in unigrams:
      for unigram in range(each.count):
          container.append(each.word2)
  if not container:
    return False
  if container:
    return True



def generateHaiku(firstWord):
<<<<<<< HEAD
	inDB = inDatabase(firstWord)
	if inDB:
		haiku = ""
		haiku += startGenerateLine(5, firstWord)
		haiku += "\n"
		haiku += startGenerateLine(7)
		haiku += "\n"
		haiku += startGenerateLine(5)
	if not inDB:
		firstWord = pickRandomWord(5)
		haiku = generateHaiku(firstWord)
	return haiku

def startGenerateLine(sylCount, base= None):
	if not base:
		base = pickRandomWord(sylCount)
	remainingSylCount = sylCount - countSyllables(base)
	line = finishGenerateLine(remainingSylCount, base)
	return line

def finishGenerateLine(sylCount, base):
=======
  inDB = inDatabase(firstWord)
  if inDB:
    haiku = ""
    haiku += generateLine(4, firstWord)
    haiku += "\n"
    haiku += generateLine(6)
    haiku += "\n"
    haiku += generateLine(4)
  if not inDB:
    firstWord = pickRandomWord(4)
    haiku = generateHaiku(firstWord)
  return haiku

def generateLine(sylCount, base= None):
>>>>>>> master
  if sylCount == 0:
    return base
  lastWord = base.rsplit(None, 1)[-1]
  possibleWords = grabPossibleWords(lastWord, sylCount)
  if possibleWords:
    index = randrange(0, len(possibleWords))
    adder = possibleWords[index]
  if not possibleWords:
    adder = pickRandomWord(sylCount)
  newBase = base + " " + adder
  workingSylCount = sylCount - countSyllables(adder)
  return finishGenerateLine(workingSylCount, newBase)

def pickRandomWord(reqSylCount):
	from models import Unigram
	lengthDB = Unigram.query.count()
	while True:
		randomNumPick = randrange(1, lengthDB)
		tryWord = Unigram.query.filter(Unigram.id == randomNumPick).first()
		if countSyllables(tryWord.word1) <= reqSylCount:
			word = tryWord.word1
			break
	return tryWord.word1


def validThing(unigram):
	pos = str(identifyPartsOfSpeech(unigram.word2))
	countSyllables(unigram.word2) == 1 &&
	pos != 'IN' && pos != "DT"


def formatPossibleWords(unigrams, reqSylCount):
	tempContainer = []
	container = []
	if reqSylCount == 1:
		tempContainer = [word in unigrams if validThing(unigram)]

		# for each in unigrams:
		# 	if countSyllables(each.word2) == 1:
		# 		tempContainer.append(each)
		# for unigram in tempContainer:
		# 	if str(identifyPartsOfSpeech(unigram.word2)) == 'IN' or str(identifyPartsOfSpeech(unigram.word2)) == 'DT':
		# 		tempContainer.remove(unigram)
		for unigram in tempContainer:
			for index in range(unigram.count):
				if countSyllables(unigram.word2) <= reqSylCount:
					container.append(unigram.word2)
	else:
		for each in unigrams:
			for index in range(each.count):
				if countSyllables(each.word2) <= reqSylCount:
					container.append(each.word2)
	return container

def grabPossibleWords(baseWord, reqSylCount):
	from models import Unigram
	listOfUnigrams = Unigram.query.filter(Unigram.word1 ==baseWord)
	return formatPossibleWords(listOfUnigrams, reqSylCount)

def identifyPartsOfSpeech(word):
	cleanString = re.sub(ur"[^\w\d'\s]+",' ', word)
	pos = nltk.word_tokenize(cleanString)
	result = nltk.pos_tag(pos)
	return result[0][1]

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
# print("***************")
print(generateHaiku("lksdjfhlsdhjfgsl;d"))
>>>>>>> master

# index of the parts of speech tags outputted by identifyingPartsOfSpeech() method
# http://www.scs.leeds.ac.uk/amalgam/tagsets/brown.html


