# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        first = pre
        second = pre

        while first != None and n >= 0:
            first = first.next
            n = n - 1

        while first != None:
            first = first.next
            second = second.next
        # print(second)
        second.next = second.next.next
        return pre.next
