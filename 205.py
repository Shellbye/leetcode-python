class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        map1 = {}
        for i in range(len(s)):
            # not mapped
            if s[i] not in map1:
                if t[i] in map1.values():
                    # t[i] is used as value
                    return False
                map1[s[i]] = t[i]  # map it
                continue
            else:
                if map1[s[i]] != t[i]:
                    return False
        return True
