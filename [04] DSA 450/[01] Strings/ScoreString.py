# https://leetcode.com/problems/score-of-a-string/
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        ord() - Converts a Character into a ASCII Value
        chr() - Converts a ASCII Value into a Character
        abs() - For Returning an Absolute Value
        """
        sum = 0
        for i in range(0, len(s) - 1):
            sum += abs(ord(s[i]) - ord(s[i+1]))
        return sum