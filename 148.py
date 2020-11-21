# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        while head and head.next:
            if head.next.val >= head.val:
                head = head.next
                continue
            cur = head.next
            pre = dummy
            while cur.val > pre.next.val:
                pre = pre.next
            
            # 当前节点被拿走
            head.next = cur.next
            # 插入 cur
            cur.next = pre.next
            pre.next = cur
        return dummy.next
