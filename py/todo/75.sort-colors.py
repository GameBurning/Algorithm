#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors
# # algorithms
# Medium (38.24%)
# Total Accepted:    182.7K
# Total Submissions: 477.8K
# Testcase Example:  '[0]'
#
# 
# Given an array with n objects colored red, white or blue, sort them so that
# objects of the same color are adjacent, with the colors in the order red,
# white and blue.
# 
# 
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# 
# 
# Note:
# You are not suppose to use the library's sort function for this problem.
# 
# 
# click to show follow up.
# 
# 
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with an one-pass algorithm using only constant space?
# 
# 
#
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        wait_0 = 0
        wait_2 = len(nums) - 1
        i = 0
        while i <= wait_2:
            if nums[i] == 0:
                nums[wait_0], nums[i] = nums[i], nums[wait_0]
                wait_0 += 1
            if nums[i] == 2:
                nums[wait_2], nums[i] = nums[i], nums[wait_2]
                wait_2 -= 1
                i -= 1
            i += 1


