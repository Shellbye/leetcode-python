import bisect
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        le = bisect.bisect_left(nums, target)
        ri = bisect.bisect_right(nums, target)
        if le == ri:
            return [-1, -1]
        return [le, ri - 1]
