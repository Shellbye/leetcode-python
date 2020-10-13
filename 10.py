class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        特殊 case 引发的思考[https://juejin.im/post/6844903897434193934]
        abe / abc*e
        上面这个 case 里，e 和 c 是不匹配的，但是最终结果却是匹配的，
        这是因为匹配过程并不要求每个子问题都匹配，只要最终结果路径上都匹配就行了
        """
        def match(i, j):
            f = i >= 1 and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
            print("i:{},j:{}, ret:{}".format(i, j, f))
            return f
        if s == p:
            return True
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(s) + 1):
            for j in range(1, len(p) + 1):
                # 因为 dp[0][0] 用来表示了空串，所以 s[i] 其实表示 s[i - 1]
                if p[j - 1] == "*":
                    # 匹配 0 次
                    dp[i][j] = dp[i][j - 2]
                    # 这个 if 比较难，应该是匹配 1 次或者 多次
                    if match(i, j - 1):
                        dp[i][j] |= dp[i - 1][j] # 这里需要用 ｜= 因为前面算过 dp[i][j] 了
                else:
                    if match(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[len(s)][len(p)]
