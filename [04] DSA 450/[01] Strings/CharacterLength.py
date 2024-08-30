# https://leetcode.com/problems/number-of-lines-to-write-string/description/
class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        line_count, line_size= 1, 0
        for char in s:
            pos = ord(char) - 97
            if line_size + widths[pos] > 100:
                line_count += 1
                line_size = widths[pos]
            else:
                line_size += widths[pos]
        return [line_count, line_size]