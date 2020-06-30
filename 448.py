class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # mark
        for v in nums:
            v = abs(v)
            nums[v - 1] = abs(nums[v - 1]) * -1

        # print(nums)
        # statistic
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans
