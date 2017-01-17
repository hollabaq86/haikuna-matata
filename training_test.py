import unittest
import training

class TestTrainingMethods(unittest.TestCase):

  def test_favor_unigram(self):
    from models import Unigram
    training.favorUnigram("the", "quick")
    unigram = Unigram.query.filter(Unigram.word1 == "the", Unigram.word2 == "quick").first()
    print int(unigram.count)
    self.assertEqual(unigram.count, 2)

  def test_unfavor_unigram(self):
    from models import Unigram
    training.unfavorUnigram("the", "quick")
    unigram = Unigram.query.filter(Unigram.word1 == "the", Unigram.word2 == "quick").first()
    print int(unigram.count)
    self.assertEqual(unigram.count, 1)


if __name__ == '__main__':
  unittest.main()
