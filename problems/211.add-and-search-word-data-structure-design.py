#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#


import collections


class WordDictionary(object):
    def __init__(self):
        self.len2words = collections.defaultdict(list)

    def addWord(self, word):
        self.len2words[len(word)].append(word)

    def search(self, word):
        words = self.len2words[len(word)]
        for i, char in enumerate(word):
            words = [w for w in words if char in ('.', w[i])]
            if not words:
                return False
        return True


wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")

wd.search("pad")
wd.search(".ad")
wd.search("b..")

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
