class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        ans = 0
        i = 0
        min_v = {}
        ans = self.doCost(cost, i, min_v)
        return ans

    def doCost(self, cost, i, min_v):
        if i in min_v:
            return min_v[i]
        c1 = c2 = 0
        if i < len(cost):
            c1 = cost[i] + self.doCost(cost, i+1, min_v)
        if i + 1 < len(cost):
            c2 = cost[i+1] + self.doCost(cost, i+2, min_v)
        # print("i:{}, c1:{}, c2:{}, cost:{}".format(i, c1, c2, cost))
        m = min(c1, c2)
        min_v[i] = m
        return m
