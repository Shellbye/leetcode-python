class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        g_idx = s_idx = 0
        while s_idx < len(s) and g_idx < len(g):
            if g[g_idx] <= s[s_idx]:
                g_idx = g_idx + 1
                s_idx = s_idx + 1
                ans = ans + 1
            else:
                s_idx = s_idx + 1
        return ans

