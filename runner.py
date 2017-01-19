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
		addWords = [each.word2 for unigram in xrange(each.count)]
		container.append(addWords)
	if not container:
		return False
	if container:
		return True

def generateHaiku(firstWord):
	inDB = inDatabase(firstWord)
	if inDB:
		haiku = startGenerateLine(5, firstWord)
		nextLineStart = haiku.split()[-1]
		haiku += "\n"
		haiku += startGenerateLine(7, haiku.split()[-1], True)
		nextLineStart = haiku.split()[-1]
		haiku += "\n"
		haiku += startGenerateLine(5, haiku.split()[-1], True)
	if not inDB:
		firstWord = pickRandomWord(5)
		haiku = generateHaiku(firstWord)
	return haiku

def startGenerateLine(sylCount, startingWord= None, repeat=None):
	if not startingWord:
		startingWord = pickRandomWord(sylCount)
	if repeat:
		possibilities = createPossibleWords(startingWord, sylCount)
		startingWord = possibilities[0]
	remainingSylCount = sylCount - countSyllables(startingWord)
	line = buildLineList(remainingSylCount, [startingWord])
	return " ".join(line)

def buildLineList(sylCount, wordsFromBefore):
	from random import shuffle
	if sylCount == 0:
		return wordsFromBefore
	lastWord = wordsFromBefore[-1]
	possibilities = createPossibleWords(lastWord, sylCount)
	for possibleWord in possibilities:
		newWordsFromBefore = [word[:] for word in wordsFromBefore]
		newWordsFromBefore.append(possibleWord)
		newSyllableCount = sylCount - countSyllables(possibleWord)
		result = buildLineList(newSyllableCount, newWordsFromBefore)
		if result:
			return result
	return None

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

def createPossibleWords(lastWord, sylCount):
	from random import shuffle
	possibilities = grabPossibleWords(lastWord, sylCount)
	shuffle(possibilities)
	return possibilities

def grabPossibleWords(baseWord, reqSylCount):
	from models import Unigram
	listOfUnigrams = Unigram.query.filter(Unigram.word1 ==baseWord)
	return filterPossibleWords(listOfUnigrams, reqSylCount)

def filterPossibleWords(unigrams, reqSylCount):
	if reqSylCount == 1 or reqSylCount == 2:
		filteredUnigrams = removePartOfSpeech(unigrams)
	filteredWords = sylCountFilter(unigrams, reqSylCount)
	return filteredWords

def removePartOfSpeech(unigrams):
	filteredUnigrams = [unigram for unigram in unigrams if identifyPartsOfSpeech(unigram.word2) not in ['IN', 'CC', 'DT']]
	return filteredUnigrams

def sylCountFilter(unigrams, reqSylCount):
	filteredWords = [unigram.word2 for unigram in unigrams if countSyllables(unigram.word2) <= reqSylCount]
	return filteredWords


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

# print("***************")
# print(generateHaiku("water"))
# print "***************"
# print(generateHaiku("hatrick"))



# index of the parts of speech tags outputted by identifyingPartsOfSpeech() method
# http://www.scs.leeds.ac.uk/amalgam/tagsets/brown.html

