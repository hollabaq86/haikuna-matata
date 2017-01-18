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

def generateHaiku(firstWord):
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

def startGenerateLine(sylCount, startingWord= None):
	if not startingWord:
		startingWord = pickRandomWord(sylCount)
	remainingSylCount = sylCount - countSyllables(startingWord)
	line = buildLineList(remainingSylCount, [startingWord])
	return " ".join(line)

def buildLineList(sylCount, wordsFromBefore):
	if sylCount == 0:
		return wordsFromBefore
	lastWord = wordsFromBefore[-1]
	possibilities = grabPossibleWords(lastWord, sylCount)
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

def formatPossibleWords(unigrams, reqSylCount):
	tempContainer = []
	container = []
	if reqSylCount == 1:
		for each in unigrams:
			if countSyllables(each.word2) == 1:
				tempContainer.append(each)
			newTempContainer = removePartOfSpeech('IN', tempContainer)
			finalTempContainer = removePartOfSpeech('DT', newTempContainer)
		for unigram in finalTempContainer:
			for index in range(unigram.count):
				if countSyllables(unigram.word2) <= reqSylCount:
					container.append(unigram.word2)
	else:
		for each in unigrams:
			for index in range(each.count):
				if countSyllables(each.word2) <= reqSylCount:
					container.append(each.word2)
	return container

def removePartOfSpeech(pos, tempContainer):
	for unigram in tempContainer:
		if str(identifyPartsOfSpeech(unigram.word2) == pos):
			tempContainer.remove(unigram)
	return tempContainer

# def formatPossibleWords(unigrams, reqSylCount):
# 	container = []
# 	for each in unigrams:
# 		for unigram in range(each.count):
# 			if reqSylCount == 1 and identifyPartsOfSpeech(each.word2) != 'DT':
# 				# container.append(each.word2)
# 				if reqSylCount == 1 and identifyPartsOfSpeech(each.word2) != 'IN':
# 					container.append(each.word2)
# 			if countSyllables(each.word2) <= reqSylCount:
# 				container.append(each.word2)
# 	return container

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

print(identifyPartsOfSpeech("upon"))
print(generateHaiku("the"))
# print("***************")
print(generateHaiku("lksdjfhlsdhjfgsl;d"))

# index of the parts of speech tags outputted by identifyingPartsOfSpeech() method
# http://www.scs.leeds.ac.uk/amalgam/tagsets/brown.html



# NOTES FROM MATT BAKER ABOUT REFACTORING
# def validThing(unigram):
# 	pos = str(identifyPartsOfSpeech(unigram.word2))
# 	countSyllables(unigram.word2) == 1 &&
# 	pos != 'IN' && pos != "DT"
# def formatPossibleWords(unigrams, reqSylCount):
# 	tempContainer = []
# 	container = []
# 	if reqSylCount == 1:
		# tempContainer = [word in unigrams if validThing(unigram)]
		# for each in unigrams:

