# https://leetcode.com/problems/faulty-keyboard/description/
class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for char in s:
            if char == 'i':
                res = res[::-1]
            else:
                res += char
        return res