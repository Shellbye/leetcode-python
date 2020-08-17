class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n
        mid = 0
        ans = 0
        while low <= high:
            mid = (low + high) / 2
            v = self.sum_pre(mid)
            # print(low, mid, high, v)
            if n == v:
                return mid
            elif n < v:
                high = mid - 1
            else:
                low = mid + 1
        if v > n:
            return mid - 1
        else:
            return mid
    
    def sum_pre(self, n):
        return n * (1 + n) / 2
