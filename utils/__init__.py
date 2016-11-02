class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __iter__(self):
        p = self
        while p:
            yield p
            p = p.next

    def to_list(self):
        return list(p.val for p in self)

    def __str__(self):
        return str(self.to_list())

    @classmethod
    def make_list(cls, A):
        if not A:
            return None
        head = cls(A[0])
        p = head
        for val in A[1:]:
            node = cls(val)
            p.next = node
            p = node
        return head


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def make_tree(cls, a):
        nodes = []
        for x in a:
            nodes.append(cls(x) if x else None)
        n = len(nodes)
        for i, node in enumerate(nodes):
            if not nodes[i]:
                continue
            if i * 2 + 1 < n:
                nodes[i].left = nodes[i * 2 + 1]
            if i * 2 + 2 < n:
                nodes[i].right = nodes[i * 2 + 2]
        return nodes[0] if nodes else None

    def __str__(self):
        return str(self.val)


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @classmethod
    def make_list(cls, a):
        return [cls(s, e) for s, e in a]

    def __repr__(self):
        return str((self.start, self.end))


if __name__ == '__main__':
    head = ListNode.make_list([1, 2, 3])
    print head

    head = ListNode.make_list([3, 2, 1])
    print head
