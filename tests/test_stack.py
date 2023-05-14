"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack, Node


class TestNode(unittest.TestCase):

    def test_init(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)

        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')

        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')
