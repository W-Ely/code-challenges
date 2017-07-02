"""Module is a challenge to determine proper-paranthetics."""


class Node(object):
    """Node data structure."""

    def __init__(self, value=None, next_node=None):
        """Init a node."""
        self.value = value
        self.next_node = next_node


class Stack(object):
    """Create a stack data structure."""

    def __init__(self, iterable=None):
        """Init a stack."""
        self.head = None

    def push(self, val):
        """Add item to stacl."""
        node = Node(val, self.head)
        self.head = node

    def pop(self):
        """Remove item from head and return value."""
        if self.head:
            val = self.head.value
            self.head = self.head.next_node
            return val


def proper_paranthetics(string):
    """Check a string for proper parenthic usage.

    Return 1 if the string is 'open'.
    Return 0 if the string is 'balanced'.
    Return -1 if the string is 'broken'.
    """
    stack = Stack()
    ref_in = {
        '(': ')', '[': ']', '<': '>', '{': '}'
    }
    ref_out = {
        ')', ']', '>', '}'
    }
    for char in string:
        if char in ref_in:
            stack.push(ref_in[char])
        if char in ref_out:
            out = stack.pop()
            if out is not char:
                return -1
    if stack.head:
        return 1
    return 0
