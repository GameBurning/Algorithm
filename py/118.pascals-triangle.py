#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle
#
# algorithms
# Easy (38.64%)
# Total Accepted:    139.7K
# Total Submissions: 361.4K
# Testcase Example:  '0'
#
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# 
# For example, given numRows = 5,
# Return
# 
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res
        res.append([1])
        for i in range(1, numRows):
             line = [1]
             for j in range(1, i):
                 line.append(res[i - 1][j - 1] + res[i - 1][j])
             line.append(1)
             res.append(line)
        return res


