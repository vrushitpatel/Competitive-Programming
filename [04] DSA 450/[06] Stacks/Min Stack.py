# https://leetcode.com/problems/min-stack/description/
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_val = [(2**31)]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val <= self.min_val[-1]:
            self.min_val.append(val)
        
    def pop(self):
        """
        :rtype: None
        """
        if self.top() == self.min_val[-1]:
            self.min_val.pop()
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()