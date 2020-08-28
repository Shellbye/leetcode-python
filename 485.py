class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        continue_one_cnt = 0
        max_c_one = 0
        for v in nums:
            if v == 1:
                continue_one_cnt = continue_one_cnt + 1
            else:
                max_c_one = max(max_c_one, continue_one_cnt)
                continue_one_cnt = 0
        return max(max_c_one, continue_one_cnt)
