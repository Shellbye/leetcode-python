class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        ans = 0
        width = len(grid[0])
        height = len(grid)
        for i in range(height):
            for j in range(width):
                print(i,j)
                if grid[i][j] == 1:
                    # left
                    if j - 1 >= 0 and grid[i][j - 1] == 0:
                        print("left")
                        ans = ans + 1
                    # right
                    if j + 1 < width and grid[i][j + 1] == 0:
                        print("right")
                        ans = ans + 1
                    # up
                    if i - 1 >= 0 and grid[i - 1][j] == 0:
                        print("up")
                        ans = ans + 1
                    # down
                    if i + 1 < height and grid[i + 1][j] == 0:
                        print("down")
                        ans = ans + 1
                    if i == 0:
                        print("up border")
                        ans = ans + 1
                    if j == 0:
                        print("left border")
                        ans = ans + 1
                    if i == height - 1:
                        print("down border")
                        ans = ans + 1
                    if j == width - 1:
                        print("right border")
                        ans = ans + 1
        return ans
