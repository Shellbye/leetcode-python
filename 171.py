class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import math
        ans = 0
        i = len(s) - 1
        for v in s:
            n = ord(v)
            ans = ans + math.pow(26, i) * (n-64)
            i = i - 1
        return int(ans)


class SolutionV2(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import math
        ans = 0
        for i in range(len(s)):
            ans = ans * 26
            ans = ans + (ord(s[i])-64)
        return int(ans)
