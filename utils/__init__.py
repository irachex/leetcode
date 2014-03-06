class ListNode:

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


if __name__ == '__main__':
    head = ListNode.make_list([1, 2, 3])
    print head

    head = ListNode.make_list([3, 2, 1])
    print head


