class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        s_set = set(s)
        w_set = set("".join(wordDict))
        if len(s_set - w_set):
            return []
        ans = []
        self.dfs(s, 0, wordDict, [], ans)
        return ans
    
    def dfs(self, s, idx, wordDict, path, ans):
        # print("idx:{}, len:{}".format(idx, len(s)))
        if idx == len(s):
            ans.append(" ".join(path))
            return
        cur = ""
        for i in range(idx, len(s)):
            cur += s[i]
            if cur in wordDict:
                # print("{} in wordDict, i+1:{}".format(cur, i + 1))
                self.dfs(s, i + 1, wordDict, path + [cur], ans)
            
