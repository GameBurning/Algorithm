#
# [325] Maximum Size Subarray Sum Equals k
#
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k
#
# algorithms
# Medium (42.42%)
# Total Accepted:    32.8K
# Total Submissions: 77.4K
# Testcase Example:  '[1,-1,5,-2,3]\n3'
#
# 
# Given an array nums and a target value k, find the maximum length of a
# subarray that sums to k. If there isn't one, return 0 instead.
# 
# 
# 
# ⁠   Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit
# signed integer range.
# 
# 
# 
# ⁠   Example 1:
# 
# 
# Given nums = [1, -1, 5, -2, 3], k = 3,
# return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the
# longest)
# 
# 
# 
# ⁠   Example 2:
# 
# 
# Given nums = [-2, -1, 2, 1], k = 1,
# return 2. (because the subarray [-1, 2] sums to 1 and is the longest)
# 
# 
# 
# ⁠   Follow Up:
# ⁠   Can you do it in O(n) time?
# 
#
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans, acc = 0, 0
        mp = {0:-1}
        for i in range(len(nums)):
            acc += nums[i]
            if acc not in mp:
                mp[acc] = i
            if acc - k in mp:
                ans = max(ans, i - mp[acc - k])
        return ans

