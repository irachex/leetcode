'''
https://leetcode.com/problems/add-and-search-word-data-structure-design/

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''


class TrieNode(object):

    def __init__(self, value=None):
        self.edges = {}
        self.value = value


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            node = p.edges.get(c)
            if node is None:
                node = p.edges[c] = TrieNode()
            p = node
        p.value = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(self.root, word, 0)

    def _search(self, p, word, dep):
        for i in xrange(dep, len(word)):
            c = word[i]
            if c == '.':
                return any(self._search(child, word, i + 1)
                           for child in p.edges.itervalues())
            node = p.edges.get(c)
            if not node:
                return False
            p = node
        return p.value is True


if __name__ == '__main__':
    d = WordDictionary()
    d.addWord("bad")
    d.addWord("dad")
    d.addWord("mad")
    assert not d.search("pad")
    assert d.search("bad")
    assert d.search(".ad")
    assert d.search("b..")
