class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or not nums[0]:
            return nums
        if len(nums) * len(nums[0]) != r * c:
            return nums
        n_row, n_col = 0, 0
        ans = [[0] * c] * r
        ans = [[0 for j in range(c)] for i in range(r)]
        for row in range(r):
            # print("row", row)
            for column in range(c):
                # print("column", column)
                # print(ans)
                # print(row, column, n_row, n_col)
                # print(ans[row][column])
                ans[row][column] = nums[n_row][n_col]
                # update row and column index
                if n_col < len(nums[0]) - 1:
                    n_col += 1
                else:
                    n_col = 0
                    n_row += 1
        return ans
