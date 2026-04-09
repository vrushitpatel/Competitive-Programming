# Missing Number
# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = []
        n = len(nums)
        res = [0 for i in range(n + 1)]
        
        for i in nums:
            res[i] = 1
            
        return res.index(0)

# ===================================================================

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_arr = sum(nums)
        optimal_sum = (n * (n + 1)) / 2
        return int(optimal_sum - sum_arr)
