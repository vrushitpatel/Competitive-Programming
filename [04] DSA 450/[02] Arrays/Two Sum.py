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