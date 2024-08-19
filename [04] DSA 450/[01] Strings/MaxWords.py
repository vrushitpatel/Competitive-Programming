# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = 0
        for sent in sentences:
            words = sent.count(" ") + 1
            if max_words < words:
                max_words = words
        return max_words
        