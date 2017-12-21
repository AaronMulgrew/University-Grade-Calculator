import unittest
import Uni_Grades_Calculator

class Test_CalcOverall(unittest.TestCase):
    def test_CalcFunc(self):
        self.assertFalse(Uni_Grades_Calculator.CalcOverall(0,0))

    def test_CalcFunc_returns_50(self):
        self.assertEqual(Uni_Grades_Calculator.CalcOverall([100], [50]), '50.0')

    def test_CalcFunc_returns_75(self):
        self.assertEqual(Uni_Grades_Calculator.CalcOverall([50, 50], [50, 100]), '75.0')

if __name__ == '__main__':
    unittest.main()
