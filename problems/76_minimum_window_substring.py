import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        table = {}

        for c in t:
            table[c] = table.get(c, 0) + 1

        begin, end = 0, 0
        counter = len(table)
        curr_length = sys.maxsize

        ans = ""

        while (end < len(s)):
            endchar = s[end]

            if endchar in table:
                table[endchar] -= 1
                if table[endchar] == 0:
                    counter -= 1

            end += 1

            while (counter == 0):
                if (end-begin < curr_length):
                    ans = s[begin:end]
                    curr_length = end-begin

                startchar = s[begin]
                if (startchar in table):
                    table[startchar] += 1
                    if table[startchar] > 0:
                        counter += 1

                begin += 1

        return ans
