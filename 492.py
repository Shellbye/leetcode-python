class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = area
        W = 1
        diff = L - W
        ans = [L, W]
        while L >= W and W * W <= area:
            L = L - 1
            if L == 0 or area % L != 0:
                continue
            W = area / L
            t_diff = abs(L - W)
            # print(L, W, t_diff)
            if t_diff < diff:
                diff = t_diff
                ans[0] = L
                ans[1] = W
        # ans.sort(reverse=True)
        return ans


class SolutionV2(object):
    import math
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        W = int(math.sqrt(area))
        
        while area % W != 0:
            W = W - 1

        return [area / W, W]
