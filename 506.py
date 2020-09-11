class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        order = nums[:]
        order.sort(reverse=True)
        for i, n in enumerate(nums):
            idx = order.index(n)
            if idx > 2:
                nums[i] = str(idx + 1)
            elif idx == 0:
                nums[i] = "Gold Medal"
            elif idx == 1:
                nums[i] = "Silver Medal"
            else:
                nums[i] = "Bronze Medal"
        return nums
