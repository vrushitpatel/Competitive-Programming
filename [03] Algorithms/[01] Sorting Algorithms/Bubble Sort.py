# https://youtu.be/M6Vg8SmGMA8?si=T3JURbPJPxuxTNAQ
# https://www.geeksforgeeks.org/problems/bubble-sort/1
# ==================================================
# Time Complexity: O(n^2) 
# Space Complexity: O(1)
# Optimized Best Case Time Complexity: O(n)
# ==================================================
# Repeatedly swaps adjacent elements that are out of order.
# ==================================================
## Ascending Order
# ==================================================
# Optimized Python program for implementation of Bubble Sort
class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        
        # Traverse through all array elements
        for i in range(n):
            swapped = False
            
            # Last i elements are already in place
            for j in range(n-i-1):
                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    
            if (swapped == False):
                break
            
        return arr

# ==================================================
## Descending Order
# ==================================================
# Optimized Python program for implementation of Bubble Sort
class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        
        # Traverse through all array elements
        for i in range(n):
            swapped = False
            
            # Last i elements are already in place
            for j in range(n-i-1):
                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if arr[j] < arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    
            if (swapped == False):
                break
            
        return arr