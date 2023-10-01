import unittest
from level_2.search_monotony import Solution

class TestSolution(unittest.TestCase):
    def test_find_unsorted_subarray(self):
        # Вхідний масив де елементи зростають монотонно
        input_array = [1, 2, 3, 4, 5]
        result = Solution.search_monotony(input_array)
        self.assertEqual(result, (True), "Помилка для масиву де елементи зростають монотонно")

        # Вхідний масив де елементи спадають монотонно.
        input_array = [5,4,3,2,1]
        result = Solution.search_monotony(input_array)
        self.assertEqual(result, (True), "Помилка для масиву де елементи спадають монотонно.")

        # Вхідний масив де елементи зростають монотонно і повторюються
        input_array = [1,1,2,3,4,4]
        result = Solution.search_monotony(input_array)
        self.assertEqual(result, (True), "Помилка для масиву де елементи зростають монотонно і повторюються")

        # Вхідний масив де елементи не є монотонними
        input_array = [1,2,3,3,2,3]
        result = Solution.search_monotony(input_array)
        self.assertEqual(result, (False), "Помилка для масиву де елементи не є монотонними")

if __name__ == '__main__':
    unittest.main()