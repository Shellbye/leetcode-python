# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        d = ListNode(-1)
        d.next = head
        while head is not None:
            if head.next is not None and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return d.next
