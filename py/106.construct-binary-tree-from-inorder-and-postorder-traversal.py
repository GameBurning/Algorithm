#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
#
# algorithms
# Medium (32.62%)
# Total Accepted:    96.9K
# Total Submissions: 297K
# Testcase Example:  '[]\n[]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        if len(postorder) == 1:
            return root
        p = inorder.index(rootVal)
        root.left = self.buildTree(inorder[:p], postorder[:p])
        root.right = self.buildTree(inorder[p + 1:], postorder[p:-1])
        return root