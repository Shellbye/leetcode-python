class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = {}
        for v in s:
            if v in m:
                m[v] = m[v] + 1
            else:
                m[v] = 1
        for v in t:
            if v not in m:
                return v
            else:
                if m[v] == 0:
                    return v
                else:
                    m[v] = m[v] - 1
        return 
