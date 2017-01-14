import unittest
import parser

class parseIntoProbabilityHashTests(unittest.TestCase):

  def testKeySetting(self):
    string2 = "This apple is red."
    one = "this apple"
    two = "apple is"
    three = "is red"
    outcome = {one: 1, two: 1, three: 1}
    probabilityHash2 = parser.parseIntoProbabilityHash(string2)
    self.assertEqual(probabilityHash2, outcome)

  def testIncrementingValue(self):
    string = "How are you doing today, my friend? Are you happy or are you sad? How are your kids doing today?"
    probabilityHash = parser.parseIntoProbabilityHash(string)
    self.assertEqual(probabilityHash["are you"], 3)

def main():
    unittest.main()

if __name__ == '__main__':
  main()
