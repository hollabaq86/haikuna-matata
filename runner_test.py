import unittest
import runner

class TestRunnerMethods(unittest.TestCase):

  def test_generate_random_haiku(self):
    haiku = generateHaiku('hello')
    self.assertIsInstance(haiku, String)

if __name__ == '__main__':
    unittest.main()
