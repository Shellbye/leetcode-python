class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        used = [False] * len(candidates)
        self.dfs(candidates, 0, [], target, ans, used)
        return ans

    def dfs(self, candidates, idx, path, target, ans, used):
        if sum(path) == target:
            ans.append(path[:])
            return
        if sum(path) > target:
            return 
        for i in range(idx, len(candidates)):
            if used[i]:
                continue
            if i > 0 and (candidates[i] == candidates[i - 1]) and not used[i - 1]:
                continue
            used[i] = True
            path.append(candidates[i])
            self.dfs(candidates, i + 1, path, target, ans, used)
            path.pop()
            used[i] = False
