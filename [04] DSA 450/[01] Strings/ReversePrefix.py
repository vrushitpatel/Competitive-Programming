# https://leetcode.com/problems/reverse-prefix-of-word/description/
class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        pos = word.find(ch) + 1
        a = word[:pos]
        b = word[pos:]
        return a[::-1] + b