#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal
#
# algorithms
# Medium (47.26%)
# Total Accepted:    224.1K
# Total Submissions: 474.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# 
# For example:
# Given binary tree [1,null,2,3],
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 
# 
# return [1,3,2].
# 
# 
# Note: Recursive solution is trivial, could you do it iteratively?
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        queue = [root]
        visited = set()
        while queue:
            node = queue.pop()
            if not node:
                continue
            if not node.left or node.left in visited:
                res.append(node.val)
                visited.add(node)
                queue.append(node.right)
            else:
                queue.append(node)
                queue.append(node.left)
        return res

