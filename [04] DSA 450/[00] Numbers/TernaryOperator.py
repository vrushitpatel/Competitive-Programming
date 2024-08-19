# Tutorial: https://www.geeksforgeeks.org/ternary-operator-in-python/#
# Question: https://leetcode.com/problems/smallest-even-multiple/
class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n%2 == 0 else n * 2