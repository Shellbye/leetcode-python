class Solution(object):
    def wordPattern(self, pattern, str_i):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m = {}
        p = list(pattern)
        s = str_i.split(" ")
        if len(p) != len(s):
            return False
        for i in range(len(p)):
            if p[i] in m:
                if m[p[i]] != s[i]:
                    return False
                continue
            else:
                if s[i] in m.values():
                    return False
                m[p[i]] = s[i]
        return True
