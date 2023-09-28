class Solution:
    @staticmethod
    def find_unsorted_subarray(nums):
        n = len(nums) - 1

        left = 0
        while left < n and nums[left] <= nums[left + 1]:
            left += 1

        if left == n:
            return (-1, -1)

        right = n
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        subarray_min = min(nums[left:right + 1])
        subarray_max = max(nums[left:right + 1])

        while left >= 0 and nums[left] > subarray_min:
            left -= 1

        while right < n and nums[right] < subarray_max:
            right += 1

        return (left + 1, right - 1)