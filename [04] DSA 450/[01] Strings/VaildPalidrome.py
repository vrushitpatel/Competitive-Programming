# https://leetcode.com/problems/valid-palindrome/description/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
#       Solution 1:
        """"
        s = s.lower()
        str1 = ""
        rev_str = ""
        for ch in s:
            if ch.isalnum():
                str1 += ch
                rev_str = ch + rev_str

        if str1 == rev_str:
            return True
        else:
            return False
        """
#       Solution 2:
        """"
        str1 = ""
        for ch in s:
            if ch.isalnum():
                str1 += ch
        str1 = str1.lower()

        if str1 == str1[::-1]:
            return True
        else:
            return False
        """
#       Solution 3:
        result = ''.join(list(filter(lambda x: x.isalnum(), s.lower())))
        return result[::-1] == result