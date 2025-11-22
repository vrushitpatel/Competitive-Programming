# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # Find Middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow points to the second half of the List

        # Reverse the Second Half of the List
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # prev holds the pointer to start of the reversed list

        # Refer to Example 1: Now we have 2 lists: [5,4] & [1,2]. 
        # So we will just with one pointer add 5 + 1 and 4 + 2
        curr = head
        max_sum = 0
        while prev:
            curr_sum = curr.val + prev.val
            if curr_sum > max_sum:
                max_sum = curr_sum
            curr = curr.next
            prev = prev.next
        return  max_sum