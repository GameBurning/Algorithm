#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree
#
# algorithms
# Easy (33.38%)
# Total Accepted:    193K
# Total Submissions: 578.1K
# Testcase Example:  '[]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if not l and not r:
            return min(l, r) + 1
        elif l:
            return l + 1
        elif r:
            return r + 1
