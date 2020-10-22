class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans
    
    def dfs(self, nums, idx, path, ans):
        ans.append(path[:])

        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, ans)
            path.pop()
