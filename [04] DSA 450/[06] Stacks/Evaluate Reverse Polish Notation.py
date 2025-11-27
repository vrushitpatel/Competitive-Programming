# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for char in tokens:
            if char in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    stack.append(num1 + num2)
                elif char == '-':
                    stack.append(num1 - num2)
                elif char == '*':
                    stack.append(num1 * num2)
                else:
                    # Runs in Python3 only
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(char))
        return stack[0]