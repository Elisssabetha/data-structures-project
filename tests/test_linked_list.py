"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedlist(unittest.TestCase):
    def test_insert_beginning(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        ll.insert_beginning({'id': 5})
        self.assertEqual(ll.head.data, {'id': 5})
        self.assertEqual(ll.tail.data, {'id': 1})

    def test_insert_at_end(self):
        ll = LinkedList()

        ll.insert_at_end({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 1})
        ll.insert_at_end({'id': 5})
        self.assertEqual(ll.tail.data, {'id': 5})
        self.assertEqual(ll.head.data, {'id': 1})

    def test_str(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 5})
        ll.insert_at_end({'id': 1})
        self.assertEqual(str(ll), "{'id': 5} -> {'id': 1} -> None")




