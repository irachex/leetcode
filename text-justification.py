'''
https://leetcode.com/problems/text-justification/

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
'''


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n = len(words)
        a = [0 for i in xrange(n)]
        for i, w in enumerate(words):
            a[i] = len(w)

        result = []
        s = 0
        line = []
        for i in xrange(n):
            if s + a[i] + len(line) <= maxWidth:
                s += a[i]
                line.append(i)
            else:
                if len(line) == 1:
                    w = words[line[0]]
                    result.append(w + ' ' * (maxWidth - len(w)))
                else:
                    t = words[line[0]]
                    n_spaces = (maxWidth - s) / (len(line) - 1)
                    n_extra_spaces = (maxWidth - s) % (len(line) - 1)

                    for j in xrange(1, n_extra_spaces + 1):
                        t += ' ' * (n_spaces + 1)
                        t += words[line[j]]
                    for j in xrange(n_extra_spaces + 1, len(line)):
                        t += ' ' * n_spaces
                        t += words[line[j]]
                    result.append(t)

                line = [i]
                s = a[i]
        if line:
            w = ' '.join(words[j] for j in line)
            w += ' ' * (maxWidth - len(w))
            result.append(w)
        return result


if __name__ == '__main__':
    def pprint(r):
        for line in r:
            print line
    f = Solution().fullJustify
    assert f([""], 2) == ['  ']
    pprint(f(["This", "is", "an", "justification.", "example", "of", "text", "justification."], 16))
    pprint(f(["This", "is", "an", "example", "of", "text", "justification."], 16))
