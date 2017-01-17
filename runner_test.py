import unittest
import runner

class TestRunnerMethods(unittest.TestCase):

  def test_count_syllables(self):
    syllables = runner.countSyllables('hello')
    self.assertEqual(syllables, 2)

  def test_is_haiku(self):
    trueHaiku = runner.isHaiku("I am a haiku trust me this is a haiku, I'm dead serious")
    falseHaiku = runner.isHaiku("I'm a donut")
    self.assertTrue(trueHaiku)
    self.assertFalse(falseHaiku)

  #def test_generate_random_haiku(self):
  #  haiku = runner.generateHaiku('the')
  #  self.assertIsInstance(haiku, basestring)
  #  self.assertEqual(haiku, 'Hello, World')

  def test_pick_random_word(self):
    word = runner.pickRandomWord(1)
    from models import Unigram
    queryWord = Unigram.query.filter(Unigram.word1 == word)[0].word1
    self.assertIsInstance(word, basestring)
    self.assertEqual(word, queryWord)

  # def test_format_possible_words(self):

  def test_generate_line(self):
    line = runner.generateLine(4, "the")
    lineSyllables = runner.countSyllables(line)
    self.assertEqual(lineSyllables, 5)

  def test_grab_possible_words(self):
    from models import Unigram
    unigrams = Unigram.query.filter(Unigram.word1 == 'the')
    possibleWords = runner.grabPossibleWords("the", 1)
    self.assertIsInstance(possibleWords, list)
    self.assertEqual(len(possibleWords), 1)


if __name__ == '__main__':
    unittest.main()
