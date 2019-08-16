class Solution:
    def findSubstring(self, s: str, words):
        if not words or not str:
            return []

        table, ans = {}, []

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
        # according to the word_size, we'll start from each character
        # example: if word_size is 2, and the string is "abcdf", we'll check starting from 'a' and 'b'
        # if we do that, we cover all combinations
        for i in range(word_size):
            begin, end = i, i
            table = dict.copy(reference)
            counter = len(table)

            while end + word_size - 1 < len(s):
                lastworld = s[end:end + word_size]

                if lastworld in table:
                    table[lastworld] -= 1
                    if table[lastworld] == 0:
                        counter -= 1

                if end - begin + word_size == window_size:
                    if counter == 0:
                        ans.append(begin)

                    firstworld = s[begin:begin + word_size]

                    if firstworld in table:
                        table[firstworld] += 1
                        if table[firstworld] > 0:
                            counter += 1

                    begin += word_size

                end += word_size

        return ans
