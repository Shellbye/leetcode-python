class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        L = len(nums)
        ans = []
        if L < 4:
            return ans
        nums.sort()
        for i in range(L-3):
            for j in range(i+1, L-2):
                f, b = j + 1, L - 1
                while f < b:
                    tmp_sum = nums[i] + nums[j] + nums[f] + nums[b]
                    if tmp_sum == target:
                        ta = [nums[i], nums[j], nums[f], nums[b]]
                        if ta not in ans:
                            ans.append(ta)
                        f = f + 1
                        b = b - 1
                    elif tmp_sum > target:
                        b = b - 1
                    else:
                        f = f + 1
        return ans


class SolutionV2(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        L = len(nums)
        ans = []
        if L < 4:
            return ans
        nums.sort()
        # print(nums)
        for i in range(L-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, L-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                f, b = j + 1, L - 1
                while f < b:
                    tmp_sum = nums[i] + nums[j] + nums[f] + nums[b]
                    if tmp_sum == target:
                        ta = [nums[i], nums[j], nums[f], nums[b]]
                        ans.append(ta)
                        f = f + 1
                        while f < L and nums[f-1] == nums[f]:
                            f = f + 1
                        b = b - 1
                        while b >= 0 and nums[b] == nums[b+1]:
                            b = b - 1
                    elif tmp_sum > target:
                        b = b - 1
                    else:
                        f = f + 1
        return ans
