class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(t) and j < len(s):
            while i < len(t) and s[j] != t[i]:
                i = i + 1
            if i >= len(t):
                return False
            j = j + 1
            i = i + 1
        if j < len(s):
            return False
        return True
