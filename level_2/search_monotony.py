class Solution:
    @staticmethod
    def search_monotony(nums):
        n = len(nums)

        is_increasing = True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                is_increasing = False
                break

        is_decreasing = True
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                is_decreasing = False
                break

        return is_increasing or is_decreasing