# https://leetcode.com/problems/truncate-sentence/description/
class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return " ".join(s.split(" ")[:k])