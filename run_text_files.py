from flask_sqlalchemy import SQLAlchemy
import re
import models
#tests will only pass if you move this declaration of the empty probability hash to inside of the parse method
probabilityHash = {}

def parseIntoProbabilityHash(text):
  stripPunctuation = ""
  for line in text:
    stripPunctuationLine = re.sub(ur"[^\w\d'\s]+",'',line)
    # stripPunctuationLine = re.sub("\b([a-zA-Z]+)\b",' ',line)
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

def createUnigram(unigramSourcePair, count):
  split_text = unigramSourcePair.split(" ")
  new_unigram = Unigram(word1 = split_text[0], word2 = split_text[1], count = count)
  db.session.add(new_unigram)
  db.session.commit()


#runner logic
def parseText(files):
  for txtfile in files:
    haikuFile = open(txtfile)
    haikus = haikuFile.readlines()
    hashed_haikus = parseIntoProbabilityHash(haikus)
    for sourcePair, count in hashed_haikus.items():
      wordArray = sourcePair.split(' ')
      unigram = Unigram.query.filter(Unigram.word1  == wordArray[0], Unigram.word2 == wordArray[1])
      if unigram != None:
        unigram.count += count
        db.session.commit()
      else:
        createUnigram(sourcePair, count)

files = ['haikus.txt', 'poetry_examples.txt']
parseText(files)
