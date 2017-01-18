import unittest
import seed_database

class parseIntoProbabilityHashTests(unittest.TestCase):

  def testKeySetting(self):
    string2 = "This apple is red."
    one = "this apple"
    two = "apple is"
    three = "is red"
    outcome = {one: 1, two: 1, three: 1}
    probabilityHash2 = seed_database.parseIntoProbabilityHash(string2)
    self.assertEqual(probabilityHash2, outcome)

  def testIncrementingValue(self):
    string = "How are you doing today, my friend? Are you happy or are you sad? How are your kids doing today?"
    probabilityHash = seed_database.parseIntoProbabilityHash(string)
    self.assertEqual(probabilityHash["are you"], 3)

  def test_formatting_hash_method(self):
    string1 = "hello there"
    string2 = "goodbye there"
    hash = {"hello there": 1}
    result1 = seed_databse.format_hash(hash, string1)
    self.assertEqual(result1, {"hello there": 2})   
    result2 = seed_databse.format_hash(hash, string2)
    self.assertEqual(result2, {"hello there": 1, "goodbye there": 1})

def main():
    unittest.main()

if __name__ == '__main__':
  main()
