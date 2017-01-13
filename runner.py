import nltk
from nltk.corpus import cmudict
import curses
from curses.ascii import isdigit
# import string
import re

d = cmudict.dict()

def numSylsInWord(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]


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

print(countSyllables("Foil wrapped burrito...is it wrong to love you so? I don't need a man."))


