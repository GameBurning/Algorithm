#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands
#
# algorithms
# Medium (34.78%)
# Total Accepted:    120.6K
# Total Submissions: 346.9K
# Testcase Example:  '["11110","11010","11000","00000"]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 11110110101100000000
# Answer: 1
# Example 2:
# 11000110000010000011
# Answer: 3
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        temp = grid[:]
        return sum(self.sink(temp, i, j) for i in range(len(temp)) for j in range(len(temp[0])))
        
    def sink(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return 0
        else:
            grid[i][j] = '0'
            self.sink(grid, i + 1, j)
            self.sink(grid, i, j + 1)
            self.sink(grid, i - 1, j)
            self.sink(grid, i, j - 1)
            return 1
        
