# https://youtu.be/-CI6Lhv1fOw?si=EyhSAO3VQTBqX1Di
# https://www.geeksforgeeks.org/problems/insertion-sort/0
# ==================================================
# Time Complexity: O(n^2) 
# Space Complexity: O(1)
# Best Case: O(n)
# ==================================================
# Builds a sorted subarray one element at a time by inserting each new element into its correct position.
# ==================================================
## Ascending Order
# ==================================================
class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(1, n):
            j = i - 1
            key = arr[i]
            # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

# ==================================================
## Descending Order
# ==================================================

class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(1, n):
            j = i - 1
            key = arr[i]
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr