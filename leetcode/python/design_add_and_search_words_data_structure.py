import collections
from typing import Dict

from mercurial.revset import children


class PrefixNode:
    def __init__(self):
        self.children: Dict = {}
        self.is_end_word: bool = False

class WordDictionary:

    def __init__(self):
        self.root = PrefixNode()

    def addWord(self, word: str) -> None:
        # p for pointer
        p = self.root

        for c in word:
            if c not in p.children:
                p.children[c] = PrefixNode()
            p = p.children[c]

        p.is_end_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root) -> bool:
            p = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in p.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in p.children:
                        return False
                    p = p.children[c]

            return p.is_end_word

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)