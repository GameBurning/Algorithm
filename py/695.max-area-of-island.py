#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island
#
# algorithms
# Easy (53.06%)
# Total Accepted:    2.5K
# Total Submissions: 4.7K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array.
# (If there is no island, the maximum area is 0.)
# 
# Example 1:
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Given the above grid, return 6.
# 
# Note the answer is not 11, because the island must be connected
# 4-directionally.
# 
# 
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# 
# 
# Note:
# The length of each dimension in the given grid does not exceed 50.
# 
#
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid, x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 0
            if grid[x][y] == 1:
                grid[x][y] = -1
                return 1 + dfs(grid,x-1,y) + dfs(grid,x+1,y) + \
                        dfs(grid,x,y-1) + dfs(grid,x,y+1)
            return 0
        if not grid:
            return 0
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(grid, i, j))
        return maxArea

        
