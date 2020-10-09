class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        if not nums:
            return ans
        m = {}
        for v in nums:
            if v in m:
                m[v] += 1
            else:
                m[v] = 1
        # print(m)
        for key in m:
            v1 = m[key]
            if key + 1 in m:
                ans = max(ans, v1 + m[key + 1])
            if key - 1 in m:
                ans = max(ans, v1 + m[key - 1])
        return ans
