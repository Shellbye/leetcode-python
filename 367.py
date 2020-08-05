class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        low, high = 0, num / 2 + 1
        while low <= high:
            mid = (low + high) / 2
            s = mid * mid
            if s == num:
                return True
            elif s < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
