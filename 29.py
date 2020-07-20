class Solution(object):
    """Time Out"""
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans = 0
        if divisor == 0:
            return 0
        d1 = abs(dividend)
        d2 = abs(divisor)
        if d2 != 1:
            while d1 - d2 >= 0:
                ans = ans + 1
                d1 = d1 - d2
        else:
            ans = d1
        if (dividend > 0 and divisor < 0) or (dividend <0 and divisor > 0):
            return -ans
        return ans


