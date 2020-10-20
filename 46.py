class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.do_permute(nums, [], ans)
        return ans
    
    def do_permute(self, nums, path, ans):
        if len(path) == len(nums):
            ans.append(path[:])
            return
        
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.do_permute(nums, path, ans)
            path.pop()
