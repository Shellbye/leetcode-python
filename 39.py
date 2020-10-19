class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        combination = []
        self.backtrack(candidates, 0, len(candidates), target, ans, combination)
        return ans
    
    def backtrack(self, candidates, start, end, target, ans, combination):
        # print(candidates, start, end, target, ans, combination)
        if 0 == target:
            ans.append(combination)
            return 
        if target < 0:
            return 
        for i in range(start, end):
            self.backtrack(candidates, i, end, target - candidates[i], ans, combination + [candidates[i]])
            # combination.pop()
