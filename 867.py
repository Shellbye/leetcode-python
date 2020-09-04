class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        w = len(A[0])
        h = len(A)
        for i in range(w):
            ans.append([0] * h)
            for j in range(h):
                ans[i][j] = A[j][i]
        return ans
