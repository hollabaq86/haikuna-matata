import re

probabilityHash = {[], ""}
#[word1, word2], count

def parseIntoProbabilityHash(text):
  stripPunctuation = re.sub(ur"[^\w\d'\s]+",' ',text)
  wordsInText = stripPunctuation.split()
  n = 0
  for word in wordsInText:
    probabilityHash[wordsInText[n]] = 1
  return probabilityHash










