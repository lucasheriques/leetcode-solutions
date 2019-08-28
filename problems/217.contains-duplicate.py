#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # first approach: use a hashtable, add the number to the hashtable
        # if the number is already there, return True
        # second approach: use a set. return len(set) != len(nums)
        # if len is different, it means the list contains non-unique values (returns True)
        return len(nums) != len(set(nums))
