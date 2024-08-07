# https://leetcode.com/problems/shuffle-string/description/
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
#       Solution 1:
        """
        result=[]
        for i in range(len(indices)):
            result.append("")
        for i in range(len(indices)):
            result[indices[i]] = s[i]
        return ''.join(result)
        """
#       Solution 2: [Liked this - Memorize it]
        """
        result = [''] * len(indices)
        for i in range(len(indices)):
            result[indices[i]] = s[i]
        return ''.join(result)
        """
#       Solution 3: [Best and Easiest Solution]
        result = ""
        for i in range(len(s)):
            result = result + s[indices.index(i)]
        return result