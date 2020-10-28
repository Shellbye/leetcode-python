class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_dis = 0
        # print(len(nums))
        for i in range(len(nums)):
            # print(i, max_dis)
            if i > max_dis:
                return False
            if max_dis >= len(nums) - 1:
                return True
            max_dis = max(max_dis, i + nums[i])
        return True



        '''V0 - time out
        if len(nums) <= 1:
            return True
        elif len(nums) == 2 and nums[0] >= 1:
            return True
        start = nums[0]
        for i in range(1, start + 1):
            if self.canJump(nums[i:]):
                return True
        return False
        '''
