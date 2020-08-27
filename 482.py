class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        ans = ""
        tmp = 1
        S = S.upper()
        for v in S[::-1]:
            if v == "-":
                continue
            ans = v + ans
            if tmp % K == 0:
                ans = "-" + ans
            tmp = tmp + 1
        if ans and ans[0] == "-":
            ans = ans[1:]
        return ans
