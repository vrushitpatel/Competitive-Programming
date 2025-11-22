# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# Approach
# 1️⃣ Count if there are at least k nodes.
# 2️⃣ Reverse the first k nodes.
# 3️⃣ Recursively call for the rest and connect.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def reverse(self, start, end):
        prev, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        count, temp = 0, head
        while temp and count < k:
            temp = temp.next
            count += 1
        if count < k:
            return head
        new_head = self.reverse(head, temp)
        head.next = self.reverseKGroup(temp, k)
        return new_head