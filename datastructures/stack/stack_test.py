from datastructures import Stack
import unittest

class TestStack(unittest.TestCase):
    def test_stack_push(self):
        stack = Stack()
        stack.push(12)
        stack.push(32)
        self.assertEqual(stack.pop(), 32)
        self.assertEqual(stack.pop(), 12)

    def test_stack_top(self):
        stack = Stack()
        stack.push(12.4)
        self.assertEqual(stack.top(), 12.4)

    def test_stack_len(self):
        stack = Stack()
        stack.push(12.4)
        self.assertEqual(len(stack), 1)

    def test_stack_empty(self):
        stack = Stack()
        self.assertTrue(stack.empty())
        stack.push(12.4)
        self.assertFalse(stack.empty())


if __name__ == '__main__':
    unittest.main()