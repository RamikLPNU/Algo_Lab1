import unittest
from find_dashboard_size import Solution

class TestSolution(unittest.TestCase):
    def test_find_dashboard_size(self):
        
        result = Solution.minimal_square_size(10, 2, 3)
        self.assertEqual(result, (9), "Помилка для test1")
        
        result = Solution.minimal_square_size(2, 1000000000, 999999999)
        self.assertEqual(result, (1999999998), "Помилка для test2")
        
        result = Solution.minimal_square_size(4, 1, 1)
        self.assertEqual(result, (2), "Помилка для test3")

if __name__ == '__main__':
    unittest.main()