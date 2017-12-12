#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
#3455555
# algorithms
# Medium (34.64%)
# Total Accepted:    120.7K
# Total Submissions: 348.6K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# 
# 
# 
# Example:
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def helpConv(head, listlen):
            if not listlen or not head:
                return None
            p = head
            for i in range((listlen - 1) // 2):
                p = p.next
            root = TreeNode(p.val)
            root.left = helpConv(head, (listlen - 1) // 2)
            root.right = helpConv(p.next, listlen // 2)
            return root
        
        if not head:
            return None
        p = head
        pf = head.next
        l = 1
        while pf and pf.next:
            p = p.next
            pf = pf.next.next
            l += 1
        if pf:
            r = l
        else:
            r = l - 1
        root = TreeNode(p.val)
        root.left = helpConv(head, l - 1)
        root.right = helpConv(p.next, r)
        return root