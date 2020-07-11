class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        if n == 0:
            return ans
        acc = 0
        while n / 26 >= 1:
            n, left = divmod(n, 26)
            print("n", n, "left", left)
            if left == 0:
                n = n - 1
                left = 26
            ans = chr(64+left) + ans
        if n > 0:
            ans = chr(64+n) + ans
        return ans
