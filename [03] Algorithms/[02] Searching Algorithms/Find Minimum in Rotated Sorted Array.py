# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# https://www.youtube.com/watch?v=_B2JakopXLc&list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&index=54
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_element = float("inf")
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= nums[high]:
                min_element = min(min_element, nums[mid])
                high = mid - 1
            else:
                min_element = min(min_element, nums[low])
                low = mid + 1
        return min_element
