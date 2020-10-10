# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        index_list = []
        for list_item in lists:
            index_list.append(list_item)
        ans = ListNode()
        cur = ans
        all_end = False
        while not all_end:
            # print("entering while")
            min_v = float('inf')
            min_n = None
            min_index = -1
            # find min
            all_end = True
            for i in range(len(index_list)):
                idx = index_list[i]
                if idx is None:
                    continue
                all_end = False
                if idx.val < min_v:
                    min_v = idx.val
                    min_n = idx
                    min_index = i    
            if all_end:
                break
            # used, move next
            # print("update min_v, ", min_v)
            index_list[min_index] = index_list[min_index].next
            # combine
            new_next = ListNode(min_v)
            cur.next = new_next
            cur = cur.next
            # print("finishing while")
            # print("ans, ", ans)
            # print("index_list, ", index_list)
            
        return ans.next
