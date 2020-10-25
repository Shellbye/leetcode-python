class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        思路
        第 i     行 变成  第 n - i 列
        第 n - i 列 变成  第 n - i 行
        并不是彼此交换
        """
        if not matrix:
            return
        n = len(matrix[0])
        # print(n)
        for row in range((n + 1)/2):
            for col in range((n)/2):
                v1 = matrix[row][col]
                matrix[row][col] = matrix[n - col - 1][row]
                matrix[n - col - 1][row] = matrix[n - row - 1][n - col - 1]
                matrix[n - row - 1][n - col - 1] = matrix[col][n - row - 1]
                matrix[col][n - row - 1] = v1
