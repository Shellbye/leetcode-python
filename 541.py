class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s 
        ans = ""
        turn = 0
        for i in range(0, len(s), k):
            if turn % 2 != 0:
                ans = ans + s[i:i+k]
            else:
                ans = ans + s[i:i+k][::-1]
            turn = turn + 1
        return ans
