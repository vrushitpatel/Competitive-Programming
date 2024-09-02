# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        ==================================
        Solution 1: 
        ==================================
        rev, flag = 0, 0
        if x < 0:
            x = x * -1
            flag = 1
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x / 10
        if abs(rev) >= (2**31) - 1:
            return 0
        if flag:
            rev *= -1
        return rev
        """
        """
        ==================================
        Solution 2: 
        ==================================
        """
        rev, flag = 0, 0
        if x < 0:
            x = x * -1
            flag = 1
        rev = int(str(x)[::-1])
        if abs(rev) >= (2**31) - 1:
            return 0
        if flag:
            rev *= -1
        return rev