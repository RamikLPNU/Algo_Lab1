def test_find_dashboard_size(self):
        # Вхідний масив де елементи зростають монотонно
        result = Solution.minimal_square_size(10, 2, 3)
        self.assertEqual(result, (9), "Помилка для масиву де елементи зростають монотонно")
        
