import unittest
import runner

class TestRunnerMethods(unittest.TestCase):

  def test_count_syllables(self):
    syllables = countSyllables('hello')
    self.assertEqual(syllables, 2)

  def test_is_haiku(self):
    trueHaiku = isHaiku("the scent not the flower is driving me crazy")
    falseHaiku = isHaiku

  def test_generate_random_haiku(self):
    haiku = generateHaiku('hello')
    self.assertIsInstance(haiku, String)
    self.assertEqual(haiku, 'Hello, World')

  def test_generate_line(self):
    line = generateLine(5, "the")
    lineSyllables = countSyllables(line)
    self.assertEqual(lineSyllables, 5)

  def test_grab_possible_words(self):
    unigrams = session.query(Unigrams).filter_by(word1 == 'the')
    possibleWords = grabPossibleWords(unigrams)
    self.assertIsInstance(possibleWords, Array)
    self.assertNotEqual(len(possibleWords), 0)


if __name__ == '__main__':
    unittest.main()
