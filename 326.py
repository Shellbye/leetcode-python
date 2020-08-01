class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 3 or n == 1:
            return True
        p = 3
        while p <= n:
            p = p * 3
            if p == n:
                return True
        return False
