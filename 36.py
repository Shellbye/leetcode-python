class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_appear = {k: set() for k in range(1, 10)}
        col_appear = {k: set() for k in range(1, 10)}
        sqr_appear = {k: set() for k in range(1, 10)}
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = board[i][j]
                if n == ".":
                    continue
                # row
                if n in row_appear[i + 1]:
                    return False
                else:
                    row_appear[i + 1].add(n)
                # col
                if n in col_appear[j + 1]:
                    return False
                else:
                    col_appear[j + 1].add(n)
                # sqr
                sqr_idx = self.get_sqr_idx(i + 1, j + 1)
                if n in sqr_appear[sqr_idx]:
                    return False
                else:
                    sqr_appear[sqr_idx].add(n)
        return True
    
    def get_sqr_idx(self, i, j):
        if i >= 1 and i <= 3:
            if j >= 1 and j <= 3:
                return 1
            if j >= 4 and j <= 6:
                return 2
            if j >= 7 and j <= 9:
                return 3
        elif i >= 4 and i <= 6:
            if j >= 1 and j <= 3:
                return 4
            if j >= 4 and j <= 6:
                return 5
            if j >= 7 and j <= 9:
                return 6
        elif i >= 7 and i <= 9:
            if j >= 1 and j <= 3:
                return 7
            if j >= 4 and j <= 6:
                return 8
            if j >= 7 and j <= 9:
                return 9
