class Solution:
    @staticmethod
    def find_unsorted_subarray(nums):
        n = len(nums) - 1

        left_increasing = 0
        left_decreasing = 0
        
        while left_increasing < n and nums[left_increasing] <= nums[left_increasing + 1]:
            left_increasing += 1
        if left_increasing == n:
            return (-1, -1)
        
        while left_decreasing < n and nums[left_decreasing] >= nums[left_decreasing + 1]:
            left_decreasing += 1
        if left_decreasing == n:
            return (-1, -1)
        
        

        right_increasing  = n
        right_decreasing  = n
        while right_increasing > 0 and nums[right_increasing] >= nums[right_increasing - 1]:
            right_increasing -= 1
        while right_decreasing > 0 and nums[right_decreasing] <= nums[right_decreasing - 1]:
            right_decreasing -= 1
            


        subarray_min_increasing = min(nums[left_increasing:right_increasing + 1])
        subarray_max_increasing = max(nums[left_increasing:right_increasing + 1])
        subarray_min_decreasing = min(nums[left_decreasing:right_decreasing + 1])
        subarray_max_decreasing = max(nums[left_decreasing:right_decreasing + 1])

        while left_increasing >= 0 and nums[left_increasing] > subarray_min_increasing:
            left_increasing -= 1
        while left_decreasing >= 0 and nums[left_decreasing] < subarray_min_decreasing:
            left_decreasing -= 1

        while right_increasing < n and nums[right_increasing] < subarray_max_increasing:
            right_increasing += 1
        while right_decreasing < n and nums[right_decreasing] > subarray_max_decreasing:
            right_decreasing += 1
            
        if left_increasing == -1 and right_increasing >= n-1:
            return (left_decreasing - 1, right_decreasing + 1)
        else:
            return (left_increasing + 1, right_increasing - 1)

        
        
        
        
    nums1 = [1,2,4,7,10,11,7,12,6,7,16,18,19]
    nums1 = [19,18,17,16,7,6,12,7,11,10,7,4,2,1]
    nums1 = [5,4,3,2,1]
    nums1 = [1,2,3,4,5]
    nums1 = [1,1,3,4,5]
    nums1 = [5,5,3,1]
    nums1 = [5]
    nums1 = [7,6,12,7,11,10,7,4,2,1]
    nums1 = [10,11,7,12,6,7,16,18,19]
    nums1 = [1,2,4,7,10,11,7,12,6]
    nums1 = [19,18,17,16,7,6,12,7,11,10]
    result = find_unsorted_subarray(nums)
    print(result) 