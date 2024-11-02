from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.testCases = {
            1: ("leetcode exercises sound delightful", True),
            2: ('eetcode', True),
            3: ('Leetcode is cool', False)
        }
        self.obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        sentence, output = self.testCases[1]
        result = self.obj.isCircularSentence(sentence = sentence)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        sentence, output = self.testCases[2]
        result = self.obj.isCircularSentence(sentence = sentence)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case3(self):
        sentence, output = self.testCases[2]
        result = self.obj.isCircularSentence(sentence = sentence)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()