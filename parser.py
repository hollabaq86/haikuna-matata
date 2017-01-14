import re
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

haikuFile = open("haikus.txt")
haikus = haikuFile.readlines()
#("word1 word2"), count
probabilityHash = {}
def parseIntoProbabilityHash(text):
  
  stripPunctuation = re.sub(ur"[^\w\d'\s]+",' ',text)
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


#print(parseIntoProbabilityHash("How are you doing today, my friend? Are you happy or are you sad? How are your kids doing today?"))

for each_line in haikus:
  parseIntoProbabilityHash(each_line)

print(probabilityHash)

def createUnigrams(hash):
  for text, counter in hash:
    split_text = text.split(" ")
    new_unigram = Unigram(word1 = split_text[0], word2 = split_text[1], count = counter)
    session.add(new_unigram)




