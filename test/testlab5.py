import unittest
from source.lab5 import solution

class TestSolutionFunction(unittest.TestCase):

    def test_solution_case_with_single_worker1(self):
        self.assertEqual(solution(6, 3, "YNN YNY YNY NYY NYY NYN"), (2))

    def test_solution_case_with_single_worker2(self):
        self.assertEqual(solution(2, 2, "YN NY"), (2))

    def test_solution_case_with_single_worker3(self):
        self.assertEqual(solution(6, 4, "YNNY NNYN YYNN NYNY NNNY NYYN"), (3))

    def test_solution_case_with_no_solution(self):
        self.assertEqual(solution(3, 2, "YNN YNN YNN"), (1))

if __name__ == '__main__':
    unittest.main()