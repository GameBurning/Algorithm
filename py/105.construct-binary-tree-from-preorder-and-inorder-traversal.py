#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
#
# algorithms
# Medium (32.85%)
# Total Accepted:    120K
# Total Submissions: 365.2K
# Testcase Example:  '[]\n[]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        if len(preorder) == 1:
            return root
        p = inorder.index(rootVal)
        root.left = self.buildTree(preorder[1: 1 + p], inorder[:p])
        root.right = self.buildTree(preorder[1 + p:], inorder[p + 1:])
        return root