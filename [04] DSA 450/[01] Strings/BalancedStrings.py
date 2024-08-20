# https://leetcode.com/problems/split-a-string-in-balanced-strings/
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        balance = 0
        for char in s:
            if char == 'R':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count