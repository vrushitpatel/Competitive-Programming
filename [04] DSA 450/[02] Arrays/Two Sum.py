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

---------------------------------------------------------------------------
Method 2:
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in nums[i+1:]:
                compliment = nums.index(compliment,i+1)
                return [i, compliment]
