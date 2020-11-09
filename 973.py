import math

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        ans = []
        m = {}
        for p in points:
            d = self.calc_d(p, [0, 0])
            if d in m:
                m[d].append(p)
            else:
                m[d] = [p]
        top_key = sorted(m.keys())
        # print(top_key)
        for k in top_key:
            ans += m.get(k)
            if len(ans) == K:
                return ans[:K]
        return ans[:K]
    
    def calc_d(self, p1, p2):
        return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
