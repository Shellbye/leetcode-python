class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        ans = [
            [1],
            [1,1]
        ]
        for i in range(2, numRows):
            t = [1]
            a = ans[-1]

            for j in range(1, i):
                t.append(a[j-1] + a[j])
            t.append(1)
            ans.append(t)
        return ans
