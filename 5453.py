class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        max_l = 0
        if left:
            max_l = max(left)
        min_r = n
        if right:
            min_r = min(right)
        return max(max_l, n - min_r)
