# Merge 2 Sorted Arrays No Duplicates Allowed
# https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1
class Solution:
    def findUnion(self, a, b):
        # code here 
        i, j = 0, 0
        n, m = len(a), len(b)
        res = []
        while i < n and j < m:
            if a[i] <= b[j]:
                if len(res) == 0 or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            else:
                if len(res) == 0 or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
                
        while i < n:
            if len(res) == 0 or res[-1] != a[i]:
                res.append(a[i])
            i += 1
            
        while j < m:
            if len(res) == 0 or res[-1] != b[j]:
                res.append(b[j])
            j += 1
        return res