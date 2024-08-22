# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        max_count = 0
        for char in s:
            if char == '(':
                count += 1
                if count > max_count:
                    max_count = count
            elif char == ')':
                count -= 1
        return max_count