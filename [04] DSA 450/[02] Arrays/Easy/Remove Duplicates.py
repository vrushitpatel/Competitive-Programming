# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        ptr = 0
        for i in range(1, len(nums)):
            if nums[ptr] != nums[i]:
                ptr += 1
                nums[ptr], nums[i] = nums[i], nums[ptr]
        return ptr + 1
