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
		haiku += "\n"
		haiku += startGenerateLine(7)
		haiku += "\n"
		haiku += startGenerateLine(5)
	if not inDB:
		firstWord = pickRandomWord(5)
		haiku = generateHaiku(firstWord)
	return haiku

def startGenerateLine(sylCount, startingWord= None):
	if not startingWord:
		startingWord = pickRandomWord(sylCount)
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
		filteredUnigrams = removeBadWords(filteredUnigrams)
		filteredWords = sylCountFilter(filteredUnigrams, reqSylCount)
		return filteredWords
	else:
		filteredWords = sylCountFilter(unigrams, reqSylCount)		
		return filteredWords

def removePartOfSpeech(unigrams):
	filteredUnigrams = [unigram for unigram in unigrams if identifyPartsOfSpeech(unigram.word2) not in ['IN', 'CC', 'DT']]
	return filteredUnigrams

def removeBadWords(unigrams):
	filteredUnigrams = [unigram for unigram in unigrams if unigram.word2 not in ['so','mr','oh','it','the', 'and', 'i', 'of', 'at', 'we', 'for', 'by', 'but', 'to', 'a', 'as', 'like', 'than', 'with', "i'm"]]
	return filteredUnigrams

def sylCountFilter(unigrams, reqSylCount):
	filteredWords = [unigram.word2 for unigram in unigrams if countSyllables(unigram.word2) <= reqSylCount]
	return filteredWords


def identifyPartsOfSpeech(word):
	cleanString = re.sub(ur"[^\w\d'\s]+",' ', word)
	pos = nltk.word_tokenize(cleanString)
	result = nltk.pos_tag(pos)
	return result[0][1]


