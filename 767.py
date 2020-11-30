import collections
import operator

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        l = len(S)
        counter=collections.Counter(S)
        for k in counter.keys():
            v = counter[k]
            if 2 * v > l + 1:
                return ""
        ans = ""
        while len(ans) < l:
            counter_s = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
            for k in counter_s[:2]:
                if k[1] == 0:
                    continue
                ans += k[0]
                counter[k[0]] -= 1
        return ans
