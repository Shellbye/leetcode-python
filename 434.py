class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        preIsBlank = True
        ans = 0
        for v in s:
            if v == " " and preIsBlank:
                continue
            elif v != " " and preIsBlank:
                ans = ans + 1
                preIsBlank = False
            elif v == " " and not preIsBlank:
                preIsBlank = True
            else:
                pass
        return ans
