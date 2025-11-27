# https://leetcode.com/problems/next-greater-element-ii/

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []
        if n == 0:
            return []
        
        for i in range(2*n, -1, -1):
            curr = i % n
            while stack and nums[stack[-1]] <= nums[curr]:
                stack.pop()
            
            if i < n and stack:
                res[i] = nums[stack[-1]]
            stack.append(curr)
        return res
