class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        nums = range(1, n + 1)
        self.dfs(nums, 0, [], ans, k, 0)
        return ans
    
    def dfs(self, nums, idx, path, ans, k, depth):
        if len(path) == k:
            # print(path)
            ans.append(path)
            return 
        for i in range(idx, len(nums)):
            # print("____" * depth, i, idx)
            if nums[i] in path:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], ans, k, depth + 1)
