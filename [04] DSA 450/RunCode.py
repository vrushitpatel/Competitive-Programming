from collections import *
from math import *

class Solution(object):
    def reversingArray(self, num):
        """
        :type n: int[]
        :rtype: int[]
        """
        num.reverse()
        return num

num = list(map(int, input("Enter the List: ").strip().split()))
sol = Solution()
print("Original List: ", num)
result = sol.reversingArray(num)
print("Output List: ", result)