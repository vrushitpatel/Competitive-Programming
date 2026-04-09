# Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[p] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
            if nums[p] != 0:
                p += 1
            