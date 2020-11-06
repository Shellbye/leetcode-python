class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # print(self.countBits(8))
        # print(self.countBits(6))
        # print(self.countBits(7))
        return sorted(arr, self.doCompare)
    
    def doCompare(self, n1, n2):
        if self.countBits(n1) > self.countBits(n2):
            return 1
        elif self.countBits(n1) < self.countBits(n2):
            return -1
        else:
            return n1 - n2
    
    def countBits(self, n):
        ans = 0
        while n:
            ans += n & 1
            n = n >> 1
        return ans
