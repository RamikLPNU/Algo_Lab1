class FindUnsorted:
    @staticmethod
    def find_unsorted_subarray(nums):
    
        left = 0
        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
            left += 1

        if left == len(nums) - 1:
            return (-1, -1)

        right = len(nums) - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        return (left, right)
