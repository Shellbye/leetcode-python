class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        intervals.sort()
        for itv in intervals:
            if ans and ans[-1]:
                if itv[0] <= ans[-1][1]:
                    if ans[-1][1] <= itv[1]:
                        ans[-1][1] = itv[1]
                    continue
            ans.append(itv)
        return ans
