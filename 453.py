class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min_n = nums[0]
        for n in nums:
            min_n = min(min_n, n)
        m_cnt = {}
        for n in nums:
            if n in m_cnt:
                m_cnt[n][0] = m_cnt[n][0] + 1
            else:
                m_cnt[n] = [1, n - min_n]
        # print(m_cnt)
        ans = 0
        for k in m_cnt:
            ans = ans + m_cnt[k][0] * m_cnt[k][1]
        return ans
