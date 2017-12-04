#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree
#
# algorithms
# Easy (53.47%)
# Total Accepted:    285.3K
# Total Submissions: 533.6K
# Testcase Example:  '[]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def help_fun(root):
            if not root:
                return 0
            else:
                return max(help_fun(root.left), help_fun(root.right)) + 1
        return help_fun(root)
