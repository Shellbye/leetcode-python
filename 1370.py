class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        if not s:
            return ""
        s = list(s)
        s.sort()
        r = False
        while s:
            pos = []
            pre = ""
            for i in range(len(s)):
                v = s[i]
                if v == pre:
                    continue
                pre = v
                pos.append(i)

            pos.reverse()
            ta = []
            for p in pos:
                ta.append(s.pop(p))

            if r:
                ans.extend(ta)
            else:
                ta.reverse()
                ans.extend(ta)
            r = not r
        return "".join(ans)

