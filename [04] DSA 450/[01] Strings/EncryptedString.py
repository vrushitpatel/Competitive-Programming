# https://leetcode.com/problems/find-the-encrypted-string/description/
class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        """
        ==============================
        Solution 1:
        
        len_str = len(s)
        result = ""
        for index in range(len_str):
            pos = (index + k) % len_str
            result += s[pos]
        return result
        ==============================
        """
        """
        Solution 2:
        """
        pos = k % len(s)
        result = s[pos:] + s[:pos]
        return result