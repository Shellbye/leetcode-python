class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n / 5 > 0:
            ans = ans + n / 5
            n = n / 5
        return ans
        # V0 超时
        # ans = 0
        # for i in range(0, n+1, 5):
        #     while i / 5 > 0 and i % 5 == 0:
        #         ans = ans + 1
        #         i = i / 5
        # return ans
