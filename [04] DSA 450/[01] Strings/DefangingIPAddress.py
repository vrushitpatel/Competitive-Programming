# https://leetcode.com/problems/defanging-an-ip-address/description/
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")