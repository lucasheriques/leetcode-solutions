#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maxf is the maximum number of ocorrences of a char
        # res will be the length of the answer
        if len(s) < 2:
            return len(s)

        maxf = res = start = 0
        count = Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            maxf = max(maxf, count[s[i]])
            if res - maxf < k:
                res += 1
            else:
                count[s[start]] -= 1
                start += 1
        return res


q = Solution()
print(q.characterReplacement("ABABB", 1))
