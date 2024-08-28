# https://leetcode.com/problems/minimize-string-length/description/
class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Solution 1:
        result = ""
        for char in s:
            if char not in result:
                result += char
        return len(result)
        """
        """
        Solution 2:
        """
        return len(set(s))