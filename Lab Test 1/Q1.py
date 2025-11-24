import sys
import unittest
from typing import Any, List


class Stack:
    """
    Simple LIFO stack with robust edge-case handling.

    Methods
    -------
    push(item):
        Push item onto stack (O(1)).
    pop():
        Pop and return top item. Raises IndexError if empty.
    peek():
        Return top item without removing. Raises IndexError if empty.
    is_empty():
        Return True if stack is empty.
    size():
        Return number of items in stack.
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        """Push item onto the stack."""
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item.
        Raises IndexError if the stack is empty to make error handling explicit.
        """
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        Raises IndexError if the stack is empty.
        """
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no elements."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return number of elements in the stack."""
        return len(self._items)

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return not self.is_empty()

    def __repr__(self):
        return f"Stack({self._items})"


# Unit tests for edge cases and normal behaviour
class TestStack(unittest.TestCase):
    def test_push_pop_lifo(self):
        s = Stack()
        s.push("a")
        s.push("b")
        s.push("c")
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.pop(), "c")
        self.assertEqual(s.pop(), "b")
        self.assertEqual(s.pop(), "a")
        self.assertTrue(s.is_empty())

    def test_peek_does_not_remove(self):
        s = Stack()
        s.push(1)
        s.push(2)
        top = s.peek()
        self.assertEqual(top, 2)
        self.assertEqual(s.size(), 2)

    def test_pop_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_peek_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.peek()

    def test_bool_and_len(self):
        s = Stack()
        self.assertFalse(bool(s))
        s.push("x")
        self.assertTrue(bool(s))
        self.assertEqual(len(s), 1)

    def test_items_are_stored(self):
        s = Stack()
        s.push({"k": "v"})
        self.assertEqual(s.peek(), {"k": "v"})


# Minimal demo / safe usage example
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    print("Top:", s.peek())       # 20
    print("Popped:", s.pop())     # 20
    print("Size:", s.size())      # 1
    try:
        # pop remaining item then pop again to show edge handling
        print("Popped:", s.pop()) # 10
        print("Popped:", s.pop()) # raises IndexError
    except IndexError as e:
        print("Handled error:", e)
