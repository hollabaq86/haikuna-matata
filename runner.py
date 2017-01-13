import nltk
from nltk.corpus import cmudict
import curses
from curses.ascii import isdigit
# import string
import re
from random import randint

d = cmudict.dict()


# this method ONLY works on words that are in the dict();
# need to tweak it
def numSylsInWord(word):
  if word.lower() in d:
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
  # else:
    #create "Contains an unrecognized word" error


# cmudict is a pronouncing dictionary for north american english words.
# it splits words into phonemes, which are shorter than syllables (e.g. the word 'cat' is split into three phonemes: K - AE - T).
# but vowels also have a "stress marker": either 0, 1, or 2, depending on the pronunciation of the word (so AE in 'cat' becomes AE1).
# the code in the answer counts the stress markers and therefore the number of the vowels - which effectively gives the number of syllables
# (in examples each syllable has exactly one vowel).


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

  #separate each word in potentialHaiku
  stripPunctuation = re.sub(ur"[^\w\d'\s]+",' ',potentialHaiku)
  # stripPunctuation = potentialHaiku.translate(None, string.punctuation)
  wordsInHaiku = stripPunctuation.split()
  syllableCount = 0
  #run each word through numSylsInWord
  #sum the syllables from each word
  for i in wordsInHaiku:
    syllableCount += numSylsInWord(i)
  return syllableCount

print(countSyllables("i love donuts"))
print(isHaiku("Foil wrapped burrito...is it wrong to love you so? I don't need a man."))
print(isHaiku("blah blah jungle"))

#Generate Haiku Method
"""
Take in a word
Start with an empty string
Query database for unigrams where first word in pair matches word (creates array of unigrams)
for each in UnigramArray
  for each in unigram count
    add word to probabilityArray

sample one from probability array that satisfies syllableCount
Add arguement (only once) and sample to string
Add/Subtract word's syllables from syllable count

return string when syllableCount == 0 || 17
"""
fakeDatabase = {}

def generateHaiku(firstWord):
  return "Hello, World"


def generateLine(sylCount, base= None):
  return base if sylCount == 0
  return "You fucked up" if sylCount < 0
  #unigrams = insert get unigrams here
  if base == None:

  possibleWords = grabPossibleWords(unigrams)
  adder = possibleWords[randint(0, len(possibleWords)]
  newBase = base + " " + adder
  newSylCount = sylCount - countSyllables(adder)
  return genLineRec(newSylCount, newBase)

def grabPossibleWords(unigrams):
  container = []
  for each in unigrams:
      for unigram in range(each.count):
        container.append(each.word2)
  return container
