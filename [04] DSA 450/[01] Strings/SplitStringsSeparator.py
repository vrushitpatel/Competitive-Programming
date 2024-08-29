# https://leetcode.com/problems/split-strings-by-separator/description/
class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        """
        ---------------------------------
        Solution 1:
        ---------------------------------
        result = []
        for word in words:
            child = word.split(separator)
            for x in child:
                if x != "":
                    result.append(x)
        return result
        ---------------------------------
        """
        """
        ---------------------------------
        Solution 2:
        ---------------------------------
        """
        l=[]
        for word in words:
            l+=[i for i in word.split(separator) if i !='']             
        return l