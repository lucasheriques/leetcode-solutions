#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            key = sorted(s)
            ans[tuple(key)].append(s)

        return list(ans.values())
