#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer
#
# algorithms
# Medium (26.27%)
# Total Accepted:    121.2K
# Total Submissions: 461.2K
# Testcase Example:  '{}'
#
# 
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# 
# 
# Return a deep copy of the list.
# 
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
            
        #first
        iter = head
        while iter != None:
            copy = RandomListNode(iter.label)
            copy.next = iter.next
            iter.next = copy
            iter = copy.next

        #second
        iter = head
        while iter is not None and iter.random is not None:
            copy = iter.next
            copy.random = iter.random.next
            iter = copy.next

        #third
        dummy = RandomListNode(0)
        dummy.next = head.next
        
        iter = head
        while iter != None:
            copyIter = iter.next
            iter.next = copyIter.next
            if copyIter.next is not None:
                copyIter.next = copyIter.next.next

        return dummy.next

