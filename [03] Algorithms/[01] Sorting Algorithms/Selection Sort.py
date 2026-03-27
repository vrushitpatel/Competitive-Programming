# https://www.geeksforgeeks.org/problems/selection-sort/1
# https://youtu.be/X8pZMsEIvJk?si=otYBnnP0XjwzoTXX
# ==================================================
# Time Complexity: O(n^2) 
# Space Complexity: O(1)
# ==================================================
# Finds the minimum element and places it at the front, repeating for each position.

## Ascending Order
class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n):
            mini_index = i
            
            for j in range(i + 1, n):
                if arr[mini_index] > arr[j]:
                    mini_index = j
            arr[i], arr[mini_index] = arr[mini_index], arr[i]


## Descending Order

class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n):
            max_index = i
            
            for j in range(i + 1, n):
                if arr[max_index] < arr[j]:
                    max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]