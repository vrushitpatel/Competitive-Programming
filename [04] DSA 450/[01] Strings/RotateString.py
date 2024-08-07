# https://leetcode.com/problems/rotate-string/description/
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
#       Solution 1:
        """
        for i in range(len(s)):
            if s == goal:
                return True
            s = s[1:] + s[0]
        return False
        """
#       Solution 2:
        """
        if len(s) != len(goal):
            return False
        return goal in s + s
        """
#       Solution 3:
        return len(s)==len(goal) and s in (goal+goal)