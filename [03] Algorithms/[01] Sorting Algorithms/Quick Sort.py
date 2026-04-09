# https://youtu.be/77tOJ3kVeS0?si=cAou50bj_wSVPtcF
# https://www.geeksforgeeks.org/problems/quick-sort/1
# ==================================================
# Time Complexity: O(n log n)
# Space Complexity: O(log n)
# Worst Case: O(n²) - [5,5,5,5,5,5,5,5,5,5,5]
# ==================================================
# Picks a Pivot, Put Pivot at its correct Position/Index, then recursively sorts partitions.
# ==================================================
## Ascending Order
# ==================================================

class Solution:
    def quickSort(self, arr, low, high):
        #code here 
        if low < high:
            p_index = self.partition(arr, low, high)
            self.quickSort(arr, low, p_index - 1)
            self.quickSort(arr, p_index + 1, high)

    def partition(self, arr, low, high):
        #code here
        pivot = arr[low]
        i = low
        j = high
        
        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[j] = arr[j], arr[low]
        return j
        

# ==================================================
## Descending Order
# ==================================================

class Solution:
    def quickSort(self, arr, low, high):
        #code here 
        if low < high:
            p_index = self.partition(arr, low, high)
            self.quickSort(arr, low, p_index - 1)
            self.quickSort(arr, p_index + 1, high)

    def partition(self, arr, low, high):
        #code here
        pivot = arr[low]
        i = low
        j = high
        
        while i < j:
            while arr[i] >= pivot and i <= high - 1:
                i += 1
            while arr[j] < pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[j] = arr[j], arr[low]
        return j
        