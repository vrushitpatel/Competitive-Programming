# https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        """
        ========================================================================
        Solution 1: Does not work.
        ========================================================================

        digit = len(str(num))
        l = len(str(num))
        result = ""
        dict_roman1 = ['I', 'X', 'C', 'M']
        dict_roman2 = ['V', 'L', 'D']
        while num > 0:
            rem = num % 10
            num = num / 10
            pos = l - digit
            if rem == 9:
                result = dict_roman1[pos] + dict_roman1[pos + 1] + result
                rem -= 9
            elif rem >= 5:
                result = dict_roman2[pos] + result
                rem -= 5
                result += dict_roman1[pos] * rem
                rem = 0
            elif rem == 4:
                result = dict_roman1[pos] + dict_roman2[pos] + result
                rem -= 4
            result = dict_roman1[pos] * rem + result
            digit -= 1
        return result  
        """
        """
        ========================================================================
        Solution 2:
        ========================================================================
        """     
        number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        counter = 0
        result = ""
        while num > 0:
            if num >= number[counter]:
                result = result + roman[counter]
                num -= number[counter]
            else:
                counter += 1
        return result