class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = len(nums)
        if L < 3:
            return
        diff = float('inf')
        ans = nums[0] + nums[1] + nums[2]
        for i in range(L - 2):
            for j in range(i + 1, L - 1):
                for k in range(j + 1, L):
                    s = nums[i] + nums[j] + nums[k]
                    d = abs(s - target)
                    if d < diff:
                        # print(nums[i], nums[j], nums[k])
                        diff = d
                        ans = s 
        return ans


class SolutionV2(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = len(nums)
        if L < 3:
            return
        nums.sort()
        # print(nums)
        min_diff = float('inf')
        ans = nums[0] + nums[1] + nums[2]
        for i in range(L):
            front, end = i + 1, L - 1
            while front < end:
                tmp_sum = nums[i] + nums[front] + nums[end]
                # print("tmp_sum", tmp_sum, i, front, end)
                if tmp_sum > target:
                    end = end - 1
                elif tmp_sum < target:
                    front = front + 1
                else:
                    return tmp_sum
                diff = abs(target - tmp_sum)
                if diff <= min_diff:
                    ans = tmp_sum
                    min_diff = diff
        return ans
