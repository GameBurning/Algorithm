#
# [694] Number of Distinct Islands
#
# https://leetcode.com/problems/number-of-distinct-islands
#
# algorithms
# Medium (40.89%)
# Total Accepted:    1.7K
# Total Submissions: 4K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
# 
# Count the number of distinct islands.  An island is considered to be the same
# as another if and only if one island can be translated (and not rotated or
# reflected) to equal the other.
# 
# Example 1:
# 
# 11000
# 11000
# 00011
# 00011
# 
# Given the above grid map, return 1.
# 
# 
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
# Notice that:
# 
# 11
# 1
# 
# and
# 
# ⁠1
# 11
# 
# are considered different island shapes, because we do not consider reflection
# / rotation.
# 
# 
# Note:
# The length of each dimension in the given grid does not exceed 50.
# 
#
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid, x, y, path):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                path.append('0')
            else:
                path.append(str(grid[x][y]))
                if grid[x][y] == 1:
                    grid[x][y] = -1
                    dfs(grid, x - 1, y, path)
                    dfs(grid, x + 1, y, path)
                    dfs(grid, x, y - 1, path)
                    dfs(grid, x, y + 1, path)

        distinct = set()
        for i, t in enumerate(grid):
            for j, v in enumerate(t):
                if v == 1:
                    path = []
                    dfs(grid, i, j, path)
                    distinct.add(''.join(path))
        return len(distinct)

