import unittest
from module.find_unsorted_subarray import Solution

class TestSolution(unittest.TestCase):
    def test_find_unsorted_subarray(self):
        # Вхідний масив вже відсортований.
        input_array = [1, 2, 3, 4, 5]
        result = Solution.find_unsorted_subarray(input_array)
        self.assertEqual(result, (-1, -1), "Помилка для відсортованого масиву")

        # Весь масив потрібно відсортувати.
        input_array = [1,2,4,7,10,11,7,12,6,7,16,18,19]
        result = Solution.find_unsorted_subarray(input_array)
        self.assertEqual(result, (3, 9), "Помилка для масиву, який потрібно відсортувати повністю")

        # Вхідний масив містить лише один елемент.
        input_array = [42]
        result = Solution.find_unsorted_subarray(input_array)
        self.assertEqual(result, (-1, -1), "Помилка для масиву з одним елементом")

        # Вхідний масив з двома однаковими елементами.
        input_array = [3, 3]
        result = Solution.find_unsorted_subarray(input_array)
        self.assertEqual(result, (-1, -1), "Помилка для масиву з двома однаковими елементами")

if __name__ == '__main__':
    unittest.main()