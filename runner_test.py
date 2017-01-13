import unittest
import runner

class TestRunnerMethods(unittest.TestCase):

  def test_count_syllables(self):
    syllables = runner.countSyllables('hello')
    self.assertEqual(syllables, 2)

  def test_is_haiku(self):
    trueHaiku = runner.isHaiku("I am a haiku trust me this is a haiku, I'm dead serious")
    falseHaiku = runner.isHaiku("I'm a donut")
    self.assertEqual(trueHaiku, true)
    self.assertEqual(falseHaiku, false)

  def test_generate_random_haiku(self):
    haiku = runner.generateHaiku('hello')
    self.assertIsInstance(haiku, String)
    self.assertEqual(haiku, 'Hello, World')

  def test_generate_line(self):
    line = runner.generateLine(5, "the")
    lineSyllables = runner.countSyllables(line)
    self.assertEqual(lineSyllables, 5)

  def test_grab_possible_words(self):
    unigrams = runner.session.query(Unigrams).filter_by(word1 == 'the')
    possibleWords = runner.grabPossibleWords(unigrams)
    self.assertIsInstance(possibleWords, Array)
    self.assertNotEqual(len(possibleWords), 0)


if __name__ == '__main__':
    unittest.main()
