import re

probabilityHash = {}
#("word1 word2"), count

def parseIntoProbabilityHash(text):
  stripPunctuation = re.sub(ur"[^\w\d'\s]+",' ',text)
  wordsInText = stripPunctuation.split()
  i = 0
  count = len(wordsInText) - 1
  while (i < count):
    word1 = wordsInText[i]
    word2 = wordsInText[i+1]
    print(word1 + " " + word2)
    probabilityHash[word1 + " " + word2] = 1
    i+=1
  return probabilityHash

print(parseIntoProbabilityHash("how are you doing today, my friend?"))









