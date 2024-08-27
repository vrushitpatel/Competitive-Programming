# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_sum = -1
        for index in range(len(num) - 2):
            if num[index] == num[index + 1] and num[index + 1] == num[index + 2]:
                if max_sum < num[index] * 3:
                    max_sum = num[index] * 3
        if max_sum == -1:
            return ""
        return str(max_sum)