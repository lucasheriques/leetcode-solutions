class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        begin, end = 0, 0
        table = {}
        maxlen = 1

        while end < len(s):
            if s[end] in table:
                # if it's a char that we already found previously,
                # keep begin in the latest one
                begin = max(table[s[end]] + 1, 1)

            # found a bigger string
            if end - begin + 1 > maxlen:
                maxlen = end - begin + 1

            table[s[end]] = end
            end += 1

        return maxlen


q = Solution()
q.lengthOfLongestSubstring("abba")
