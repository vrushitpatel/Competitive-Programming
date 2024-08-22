# https://leetcode.com/problems/snake-in-matrix/description/
class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        i, j = 0, 0
        for command in commands:
            if command == "UP": i -= 1
            elif command == "DOWN": i += 1
            elif command == "RIGHT": j += 1
            else: j -= 1
        return (i * n) + j