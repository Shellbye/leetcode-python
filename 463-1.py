class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        h = len(grid)
        w = len(grid[0])
        if h == 0 or w == 0:
            return ans
        
        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    ans += self.calc_island(i, j, h, w, grid)
        return ans
    
    def calc_island(self, i, j, h, w, grid):
        r = 0
        # up
        if i == 0 or grid[i - 1][j] == 0:
            r += 1
        # left
        if j == 0 or grid[i][j - 1] == 0:
            r += 1
        # right
        if j == w - 1 or grid[i][j+1] == 0:
            r += 1
        # down
        if i == h - 1 or grid[i + 1][j] == 0:
            r += 1
        # print(i, j, r)
        return r

