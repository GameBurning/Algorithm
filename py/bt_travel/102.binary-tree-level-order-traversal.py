#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal
#
# algorithms
# Medium (40.40%)
# Total Accepted:    192.2K
# Total Submissions: 475.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        level = {root:0}
        res = []
        while queue:
            n = queue.pop(0)
            if level[n] + 1 > len(res):
                res.append([n.val])
            else:
                res[level[n]].append(n.val)
            for child in (n.left, n.right):
               	if child:
                    queue.append(child)
    	    	    level[child]=level[n]+1
        return res
