# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/
# https://youtu.be/o3luQXt08W8?si=HEB6LnzYA0wQxcIe
# ======================================================================
## Method 1 - O(n^2)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maximum = nums[0]
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                sum_sub = sum(nums[i:j + 1])
                maximum = max(maximum, sum_sub)
            
        return maximum

# ======================================================================
## Method 2 - O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maximum = float('-inf')
        sub_max = 0
        n = len(nums)
        for i in range(n):
            sub_max += nums[i]
            maximum = max(maximum, sub_max)
            if sub_max < 0:
                sub_max = 0
        
        return maximum
