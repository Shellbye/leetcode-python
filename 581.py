class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start = 0
        end = len(nums) - 1

        max_v = nums[0]
        for i in range(len(nums)):
            if nums[i] < max_v:
                # print("start:{}".format(i))
                start = i 
            max_v = max(max_v, nums[i])
        min_v = nums[-1]
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > min_v:
                # print("end:{}".format(j))
                end = j
            min_v = min(min_v, nums[j])
        if start <= end:
            return 0
        return start - end + 1
