class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        ap = set()
        ans_v = set()
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in ap:
                ap.add(s[i])
                ans_v.add(s[i])
            else:
                if s[i] in ans_v:
                    ans_v.remove(s[i])
        
        for i in range(len(s)):
            if s[i] in ans_v:
                return i 
        return -1
