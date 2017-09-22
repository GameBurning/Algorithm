#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title
#
# algorithms
# Easy (26.16%)
# Total Accepted:    111K
# Total Submissions: 424.2K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases.
#
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        return self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))
