# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
        ptr = 0
        for i in range(1, n):
            if nums[i] == nums[ptr]:
                continue
            ptr += 1
            nums[i], nums[ptr] = nums[ptr], nums[i]
        return ptr + 1