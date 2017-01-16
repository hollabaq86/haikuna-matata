from flask_sqlalchemy import SQLAlchemy
import re

#tests will only pass if you move this declaration of the empty probability hash to inside of the parse method
probabilityHash = {}

def parseIntoProbabilityHash(text):
  stripPunctuation = ""
  for line in text:
    stripPunctuationLine = re.sub("\b([a-zA-Z]+)\b",' ',line)
    stripPunctuation += stripPunctuationLine
  wordsInText = stripPunctuation.split()
  i = 0
  count = len(wordsInText) - 1
  while (i < count):
    word1 = wordsInText[i].lower()
    word2 = wordsInText[i+1].lower()
    if (word1 + " " + word2) in probabilityHash:
      probabilityHash[word1 + " " + word2] += 1
    else:
      probabilityHash[word1 + " " + word2] = 1
    i+=1
  return probabilityHash

