import unittest
from module.find_unsorted_subarray import FindUnsorted

class TestFindUnsorted(unittest.TestCase):
    def test_find_unsorted_subarray(self):
        # Вхідний масив вже відсортований.
        input_array = [1, 2, 3, 4, 5]
        result = FindUnsorted.find_unsorted_subarray(input_array)
        self.assertEqual(result, (-1, -1), "Помилка для відсортованого масиву")

        # Весь масив потрібно відсортувати.
        input_array = [5, 4, 3, 2, 1]
        result = FindUnsorted.find_unsorted_subarray(input_array)
        self.assertEqual(result, (0, 4), "Помилка для масиву, який потрібно відсортувати повністю")

        # Вхідний масив містить лише один елемент.
        input_array = [42]
        result = FindUnsorted.find_unsorted_subarray(input_array)
        self.assertEqual(result, (-1, -1), "Помилка для масиву з одним елементом")

        # Вхідний масив з двома однаковими елементами.
        input_array = [3, 3]
        result = FindUnsorted.find_unsorted_subarray(input_array)
        self.assertEqual(result, (-1, -1), "Помилка для масиву з двома однаковими елементами")


if __name__ == '__main__':
    unittest.main()
