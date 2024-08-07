# https://leetcode.com/problems/reverse-string/description/
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
#       Solution 1:
        """
        front = 0
        end = len(s) - 1
        while front < end:
            temp = s[end]
            s[end] = s[front]
            s[front] = temp
            front += 1
            end -= 1
        return s
        """
#       Solution 2:
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s
        """
#       Solution 3:
        return s.reverse()