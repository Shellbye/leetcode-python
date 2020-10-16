class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            # print("left:{} mid:{}[{}] right:{}".format(left, mid, nums[mid], right))
            if target == nums[mid]:
                return mid
            if nums[0] > nums[mid]:
                if target > nums[mid] and target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[0]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
