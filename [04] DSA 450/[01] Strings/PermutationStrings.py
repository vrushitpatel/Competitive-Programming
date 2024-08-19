# https://leetcode.com/problems/permutation-difference-between-two-strings/description/
class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            result += abs(i - t.find(s[i]))
        return result