import sys


class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []

        table = {}

        for c in p:
            table[c] = table.get(c, 0) + 1

        begin, end = 0, 0
        counter = len(table)

        ans = []

        while end < len(s):
            endchar = s[end]

            if endchar in table:
                table[endchar] -= 1
                if table[endchar] == 0:
                    counter -= 1

            end += 1

            # all characters are in the substring, but not necessarily an anagram
            while counter == 0:
                possible = s[begin:end]
                beginchar = s[begin]

                # if its an anagram, add answer
                if len(possible) == len(p):
                    ans.append(begin)
                    table[beginchar] += 1
                    counter += 1

                # not an anagram, add back beginchar to table
                elif beginchar in table:
                    table[beginchar] += 1
                    if table[beginchar] > 0:
                        counter += 1

                begin += 1

        return ans
