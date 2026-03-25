# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):

        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head

        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        
        dummy = ListNode(0, head)

        prev, cur = dummy, head
        index = 0

        while cur and index != n:
            cur = cur.next
            index += 1

        while cur:
            cur = cur.next
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next
"""

