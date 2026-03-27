# https://leetcode.com/problems/search-insert-position/

# Simply find the Lower Bound

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        lb = len(nums)

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1

        return lb