class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                j = i
                while j < len(nums) and nums[i - 1] < nums[j]:
                    j += 1
                j -= 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                
                nums[i:] = sorted(nums[i:])
                return
        return nums.sort()
