import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertIsNone(stack.top.next_node.next_node.next_node)

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        data = stack.pop()

        # стэк стал пустой
        assert stack.top is None
        assert data == 'data1'
        self.assertIsNone(stack.top)
        self.assertEqual(data, 'data1')

        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()

        # теперь последний элемента содержит данные data1
        self.assertEqual(stack.top.data, 'data1')

        # данные удаленного элемента
        self.assertEqual(data, 'data2')
