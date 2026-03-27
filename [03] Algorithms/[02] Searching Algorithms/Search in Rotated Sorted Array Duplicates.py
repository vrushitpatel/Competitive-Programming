# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
# https://www.youtube.com/watch?v=oVcBXszcpYs&list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&index=53

# Edge cases to check: [7, 7, 7, 7, 7, 7, 7, 1, 7, 7, 7, 7, 7, 7]

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                low = low + 1
                high = high - 1
                continue
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False