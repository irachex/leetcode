'''
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.
'''


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.edges = {}
        self.value = None


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            node = p.edges.get(c)
            if node is None:
                p.edges[c] = node = TrieNode()
            p = node
        p.value = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            p = p.edges.get(c)
            if p is None:
                return False
        return p.value is not None

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            p = p.edges.get(c)
            if p is None:
                return False
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("somestring")
    assert not trie.search("key")
    assert trie.search('somestring')
    assert not trie.startsWith('a')
    assert trie.startsWith('s')
    assert trie.startsWith('somes')
    assert not trie.startsWith('somestringx')
