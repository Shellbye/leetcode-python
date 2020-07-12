class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        to_front = []
        k = k % len(nums)
        bk_idx = k
        while bk_idx >= 1:
            to_front.append(nums[-bk_idx])
            bk_idx = bk_idx - 1
        
        i = len(nums) - 1 - k
        while i >= 0:
            nums[i+k] = nums[i]
            i = i - 1

        L2 = len(to_front)
        for i in range(L2):
            nums[i] = to_front[i]
