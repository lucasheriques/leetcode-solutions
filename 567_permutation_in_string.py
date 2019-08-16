class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) > len(s2):
            return False

        table = {}

        for c in s1:
            table[c] = table.get(c, 0) + 1

        begin, end, counter = 0, 0, len(table)

        while end < len(s2):
            if s2[end] in table:
                table[s2[end]] -= 1
                if table[s2[end]] == 0:
                    counter -= 1

            while counter == 0:
                if end - begin + 1 == len(s1):
                    return True

                if s2[begin] in table:
                    table[s2[begin]] += 1
                    if table[s2[begin]] > 0:
                        counter += 1

                begin += 1

            end += 1

        return False
