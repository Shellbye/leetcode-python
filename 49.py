class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = []
        m = {}
        for s in strs:
            k = "".join(sorted(s))
            if k in m:
                m[k].append(s)
            else:
                m[k] = [s]
        # print(m)
        for v in m.values():
            ret.append(v)
        return ret
