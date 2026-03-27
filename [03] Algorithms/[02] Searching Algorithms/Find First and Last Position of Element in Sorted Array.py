# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution:
    def lowerBound(self, nums, target) -> int:
        low, high = 0, len(nums) - 1
        lb = len(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    def upperBound(self, nums, target) -> int:
        low, high = 0, len(nums) - 1
        ub = len(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums, target)
        ub = self.upperBound(nums, target)
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        return [lb, ub - 1]