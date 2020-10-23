class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(1, n + 1)
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        path = []
        self.dfs(nums, 0, path, k, factorial)
        # print(path)
        r = "".join([str(i) for i in path])
        # print(r)
        return r
    
    def dfs(self, nums, idx, path, k, factorial):
        cnt = factorial[len(nums) - 1 - idx]
        if idx == len(nums):
            return
        for i in range(0, len(nums)):
            if nums[i] in path:
                continue
            if cnt < k:
                k -= cnt
                continue
            path.append(nums[i])
            self.dfs(nums, idx + 1, path, k, factorial)
            return


class SolutionV2(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(1, n + 1)
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        path = []
        self.dfs(nums, 0, path, k, factorial)
        # print(path)
        r = "".join([str(i) for i in path])
        # print(r)
        return r
    
    def dfs(self, nums, idx, path, k, factorial):
        cnt = factorial[len(nums) - 1 - idx]
        if idx == len(nums):
            return
        for i in range(0, len(nums)):
            if nums[i] in path:
                continue
            if cnt < k:
                k -= cnt
                continue
            path.append(nums[i])
            self.dfs(nums, idx + 1, path, k, factorial)
            return
