import bisect

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        pre_sum = [0]
        ans = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            ans += bisect.bisect_right(pre_sum, s - lower) - bisect.bisect_left(pre_sum, s - upper)
            pre_sum.append(s)
            pre_sum.sort()
        return ans

        '''超时
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s = sum(nums[i:j + 1])
                if s >= lower and s <= upper:
                    ans += 1
        return ans
        '''
