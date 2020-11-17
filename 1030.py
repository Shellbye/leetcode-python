class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(R):
            for j in range(C):
                ans.append(([i, j], abs(i - r0) + abs(j - c0)))
        ans.sort(cmp=lambda x, y: x[1] - y[1])
        ret = [x[0] for x in ans]
        return ret
