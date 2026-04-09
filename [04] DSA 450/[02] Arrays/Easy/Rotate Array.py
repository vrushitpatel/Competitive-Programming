# Rotate Array
# https://leetcode.com/problems/rotate-array/description/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # Cancel out Rotations
        nums[:] = nums[(n - k): ] + nums[:(n - k)]

# ==========================================================

# Without Using Slicing
# https://youtu.be/HRzQK5TkrZM?si=MwAIzg87ztzztmiJ
class Solution:
    def reverse(self, nums: List[int], low, high) -> List[int]:
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1

        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums = self.reverse(nums,(n - k), (n - 1))
        nums = self.reverse(nums, 0, (n - k -1))
        nums = self.reverse(nums, 0, (n - 1))