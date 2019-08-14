class Solution:
    def findSubstring(self, s: str, words):
        if not words or not str:
            return []

        table = {}
        ans = []

        window_size = 0
        word_size = len(words[0])

        for word in words:
            window_size += len(word)
            table[word] = table.get(word, 0) + 1

        reference = dict.copy(table)

        begin, end, counter = 0, 0, len(table)

        if len(s) < window_size:
            return ans

        # increment begin and end based on word_size
        for i in range(word_size):
            begin, end = i, i
            table = reference
            counter = len(table)

            while end + word_size - 1 < len(s):
                lastworld = s[end:word_size + end]

                if lastworld in table:
                    table[lastworld] -= 1
                    if table[lastworld] == 0:
                        counter -= 1

                if end - begin + word_size == window_size:
                    if counter == 0:
                        ans.append(begin)

                    firstworld = s[begin:word_size+begin]

                    if firstworld in table:
                        table[firstworld] += 1
                        if table[firstworld] > 0:
                            counter += 1

                    begin += word_size

                end += word_size

        return ans


q = Solution()
print(q.findSubstring("barfoothefoobarman", ['foo', 'bar']))
print(q.findSubstring("ababaab", ["ab", "ba", "ba"]))
