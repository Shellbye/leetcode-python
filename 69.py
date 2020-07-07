class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        i = 1
        while i * i <= x:
            i = i + 1
        return i - 1
        
    def mySqrtV2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        low = 1
        high = x
        ans = 0
        while low <= high:
            mid = (low + high) / 2
            m = mid * mid
            if m <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
