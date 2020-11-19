class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p_idx] = nums[i]
                p_idx += 1
        for i in range(p_idx, len(nums)):
            nums[i] = 0
        return nums
