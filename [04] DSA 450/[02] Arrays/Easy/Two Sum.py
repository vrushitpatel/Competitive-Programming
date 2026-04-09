# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_arr = len(nums)
        for i in range(len_arr):
            for j in range(i+1, len_arr):
                if ( nums[i] + nums[j] ) == target:
                    return [i, j]
        return False
# Time Complexity: O(n^2)

# ================================================
## Method 2: O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in nums[i+1:]:
                compliment = nums.index(compliment,i+1)
                return [i, compliment]

# ================================================
## Method 3: O(n)
### Hash Maps / Dictonary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict1 = {}
        for i in range(n):
            rem = target-nums[i]
            if rem in dict1:
                return [dict1[rem], i]
            else:
                dict1[nums[i]] = i