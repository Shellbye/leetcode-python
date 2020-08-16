class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return float('-inf')
        max_1 = float('-inf')
        for v in nums:
            if v > max_1:
                max_1 = v
        max_2 = float('-inf')
        for v in nums:
            if v == max_1:
                continue
            if v > max_2:
                max_2 = v
        max_3 = float('-inf')
        for v in nums:
            if v in [max_2, max_1]:
                continue
            if v > max_3:
                max_3 = v
        if max_3 == float('-inf'):
            max_3 = max_1
        return max_3
