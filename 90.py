class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans
    
    def dfs(self, nums, idx, path, ans):
        ans.append(path[:])
        for i in range(idx, len(nums)):
            if i > idx and (nums[i] == nums[i - 1]):
                continue
            self.dfs(nums, i + 1, path + [nums[i]], ans)
