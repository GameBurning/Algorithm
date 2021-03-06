#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree
#
# algorithms
# Easy (37.96%)
# Total Accepted:    202.5K
# Total Submissions: 533.5K
# Testcase Example:  '[]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# 
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.result = True
        
        def helpHeight(root):
            if not root:
                return 0
            else:
                l = helpHeight(root.left)
                r = helpHeight(root.right)
                if abs(l - r) > 1:
                    self.result = False
                return max(l, r) + 1

        helpHeight(root)
        return self.result
