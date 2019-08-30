#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        table = Counter(s1)

        begin = end = 0
        counter = len(table)

        while end < len(s2):
            endchar = s2[end]

            if endchar in table:
                table[endchar] -= 1
                if table[endchar] == 0:
                    counter -= 1

            end += 1

            while counter == 0:
                if len(s1) == end - begin:
                    return True

                beginchar = s2[begin]

                if beginchar in table:
                    table[beginchar] += 1
                    if table[beginchar] > 0:
                        counter += 1

                begin += 1

        return False
