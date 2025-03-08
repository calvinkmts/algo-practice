from typing import Dict


class TrieNode:
    def __init__(self):
        self.children: Dict = {}
        self.is_end_of_word: bool = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True

    # def __init__(self):
    #     self.hash_table = dict()
    #
    # def insert(self, word: str) -> None:
    #     self.hash_table[word] = True
    #
    # def search(self, word: str) -> bool:
    #     if self.hash_table.get(word):
    #         return True
    #
    #     return False
    #
    # def startsWith(self, prefix: str) -> bool:
    #     keys = self.hash_table.keys()
    #
    #     for key in keys:
    #         if key.startswith(prefix):
    #             return True
    #
    #     return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)