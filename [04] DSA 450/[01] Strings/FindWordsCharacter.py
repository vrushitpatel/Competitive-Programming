# https://leetcode.com/problems/find-words-containing-character/description/
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        result = []
        for index, word in enumerate(words):
            if x in word:
                result.append(index)
        return result