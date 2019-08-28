class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        begin, end = 0, 0
        table = {}
        maxlen = 1

        while end < len(s):
            if s[end] in table:
                begin = max(table[s[end]] + 1, begin)

            # test if found a bigger string
            maxlen = max(maxlen, end - begin + 1)

            table[s[end]] = end
            end += 1

        return maxlen


q = Solution()
print(q.lengthOfLongestSubstring("adbccba"))
