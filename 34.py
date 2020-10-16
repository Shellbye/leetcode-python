class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        smaller_index = self.binarySearch(nums, target - 1)
        if smaller_index < 0:
            smaller_index = 0
        # print(smaller_index)
        while smaller_index < len(nums) and nums[smaller_index] != target:
            smaller_index += 1
        if smaller_index == len(nums):
            return [-1, -1]
        end = smaller_index
        while end < len(nums) and nums[end] == target:
            end += 1
        return [smaller_index, end - 1]
    
    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
