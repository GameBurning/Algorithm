#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree
#
# algorithms
# Easy (39.54%)
# Total Accepted:    211.4K
# Total Submissions: 534.6K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.helpSymmetric(root.left, root.right)
        
    def helpSymmetric(self, left, right):
        if left and right:
            if left.val == right.val:
                return self.helpSymmetric(left.left, right.right) and self.helpSymmetric(left.right, right.left)
            else:
                return False
        elif not left and not right:
            return True
        else:
            return False
        
