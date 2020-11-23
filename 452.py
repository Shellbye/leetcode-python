class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort()
        # print(points)
        cur_begin, cur_end = points[0]
        cnt = 1
        for p in points:
            # print(cur_begin, cur_end)
            if p[0] >= cur_begin and p[0] <= cur_end:
                cur_begin = max(p[0], cur_begin)
                cur_end = min(p[1], cur_end)
                continue
            if p[1] >= cur_begin and p[1] <= cur_end:
                cur_begin = max(p[0], cur_begin)
                cur_end = min(p[1], cur_end)
                continue
            # print(p, "need one")
            cur_begin, cur_end = p
            cnt += 1
        return cnt
