class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # print(nums)
        L = len(nums)
        for v in nums:
            # print("-v",v)
            if v == L or -(v+1) == L:
                continue
            if v >= 0:
                nums[v] = -nums[v]-1
            else:
                nums[-(v+1)] = -nums[-(v+1)]-1
            # print("=", nums)
        # print(nums)
        for i in range(L):
            if nums[i] > -1:
                return i
        return L 
