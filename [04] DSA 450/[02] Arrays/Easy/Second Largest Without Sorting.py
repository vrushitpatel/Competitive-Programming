# https://www.geeksforgeeks.org/problems/second-largest3735/1

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        large1 = -1
        large2 = -1
        
        for i in arr:
            if i > large1:
                large2 = large1
                large1 = i
            elif i > large2 and i != large1:
                large2 = i
        return large2