import unittest
import runner

class TestRunnerMethods(unittest.TestCase):

  def test_count_syllables(self):
    syllables = countSyllables('hello')

  def test_generate_random_haiku(self):
    haiku = generateHaiku('hello')
    self.assertIsInstance(haiku, String)
    self.assertEqual(haiku, 'Hello, World')

  def test_generate_line(self):


if __name__ == '__main__':
    unittest.main()
