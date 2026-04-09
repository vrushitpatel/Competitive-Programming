# https://youtu.be/ZDCoxXeksWM?si=QxKf9FKI9erO8d6h [Very Important]
# https://leetcode.com/problems/sort-an-array/description/
# ==================================================
# Time Complexity: O(n log n) Best & Worst
# Space Complexity: O(1)
# ==================================================
# Divides array into two halves, recursively sorts each, then merges them.
# Watch Video to understand complexity as well
# ==================================================
## Ascending Order
# ==================================================

class Solution:
    def mergeArray(self, left_arr, right_arr):
        i, j = 0, 0
        n, m = len(left_arr), len(right_arr)
        res = []
        while i < n and j < m:
            if left_arr[i] <= right_arr[j]:
                res.append(left_arr[i])
                i += 1
            else:
                res.append(right_arr[j])
                j += 1
        while i < n:
            res.append(left_arr[i])
            i += 1
        while j < m:
            res.append(right_arr[j])
            j += 1
            
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        #code here
        
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        
        left_side = self.sortArray(left)
        right_side = self.sortArray(right)
        
        return self.mergeArray(left_side, right_side)

# ==================================================
## Descending Order
# ==================================================

class Solution:
    def mergeArray(self, left_arr, right_arr):
        i, j = 0, 0
        n, m = len(left_arr), len(right_arr)
        res = []
        while i < n and j < m:
            if left_arr[i] >= right_arr[j]:
                res.append(left_arr[i])
                i += 1
            else:
                res.append(right_arr[j])
                j += 1
        while i < n:
            res.append(left_arr[i])
            i += 1
        while j < m:
            res.append(right_arr[j])
            j += 1
            
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        #code here
        
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        
        left_side = self.sortArray(left)
        right_side = self.sortArray(right)
        
        return self.mergeArray(left_side, right_side)