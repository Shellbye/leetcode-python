class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        used = set()
        while n not in used:
            used.add(n)
            s_sum = 0
            while n > 0:
                c = n % 10
                s_sum = s_sum + c * c 
                n = n / 10
            n = s_sum
            if s_sum == 1:
                return True
        return False
