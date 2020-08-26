class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = 1
        while b <= num:
            b = b << 1
        return num ^ (b - 1)
