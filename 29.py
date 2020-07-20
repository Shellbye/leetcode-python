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


class SolutionV2(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans = 0
        if divisor == 0:
            return 0
        if divisor == 1:
            return dividend
        d1 = abs(dividend)
        d2 = abs(divisor)
        if d2 == 1:
            ans = d1
            if d1 == 2147483648:
                ans = 2147483647
        else:
            ans = self.diver(d1, d2)
            
        if (dividend > 0 and divisor < 0) or (dividend <0 and divisor > 0):
            return -ans
        return ans

    def diver(self, d1, d2):
        """60/8 = (60-32)/8 + 4 = (60-32-16)/8 + 2 + 4 = 1 + 2 + 4 = 7"""
        d3 = d2
        if d1 < d3:
            return 0
        times = 1
        while d3 + d3 < d1:
            d3 = d3 + d3
            times = times + times
        return times + self.diver(d1-d3, d2)
