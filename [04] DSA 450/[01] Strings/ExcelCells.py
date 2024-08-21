# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/
class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(ord(s[0]), ord(s[3]) + 1):
            for j in range(int(s[1]), int(s[4]) + 1):
                result.append(chr(i) + str(j))
        return result