import nltk
from nltk.corpus import cmudict
import curses
from curses.ascii import isdigit

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
  wordsInHaiku = potentialHaiku.split()
  #run each word through numSylsInWord
  for i in wordsInHaiku:
    numSylsInWord(i)



  return syllableCount
