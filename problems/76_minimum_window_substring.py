from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not s or not t:
            return ""

        table = Counter(t)
        counter = len(table)

        begin = end = 0

        response = (0, len(s))

        while end < len(s):
            endchar = s[end]

            if endchar in table:
                table[endchar] -= 1
                if table[endchar] == 0:
                    counter -= 1

            end += 1

            while counter == 0:
                if response[1] - response[0] > end - begin:
                    response = (begin, end)

                beginchar = s[begin]

                if beginchar in table:
                    table[beginchar] += 1
                    if table[beginchar] > 0:
                        counter += 1

                begin += 1

        return s[response[0]:response[1]]


Solution().minWindow("ab", "b")
