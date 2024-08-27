# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/
class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        while True:
            if "AB" in s:
                s = s.replace("AB", "")
            elif "CD" in s:
                s = s.replace("CD", "")
            else:
                break
        return len(s)