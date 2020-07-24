class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        for i in range(len(nums)):
            v = nums[i]
            if v in d and abs(d[v] - i) <= k:
                return True
            else:
                d[nums[i]] = i
        return False
        # 超时
        # if k == 0:
        #     return False
        # dup = []
        # for v in nums:
        #     if v in dup:
        #         return True
        #     else:
        #         if len(dup) >= k:
        #             dup.pop()
        #         dup.insert(0, v)
        # return False
        # 超时
        # for i in range(len(nums)):
        #     for j in range(i+1, i+1+k):
        #         if j < len(nums) and nums[i] == nums[j]:
        #             return True
        # return False
