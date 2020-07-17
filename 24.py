# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        ld_node = ListNode(-1)
        ld_node.next = head
        front = head
        back = head.next
        f = ld_node
        while front and back:
            # transfer
            f.next = back
            front.next = back.next
            back.next = front

            # move on
            f = front
            front = front.next
            if not front or not front.next:
                break
            back = front.next
            
        return ld_node.next
