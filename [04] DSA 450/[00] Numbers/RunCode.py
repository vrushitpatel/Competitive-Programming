from collections import *
from math import *

class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n%2 == 0 else n * 2

num = int(input("Enter a Number: "))
sol = Solution()
result = sol.smallestEvenMultiple(num)
print(result)