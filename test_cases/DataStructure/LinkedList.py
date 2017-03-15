import unittest

from DataStructure.LinkedList import Node, LinkedList


class TestNode(unittest.TestCase):

    def test_set_get(self):
        n = Node(5)
        assert(n.get_item() == 5)

        n = n.set_item(7)
        assert(n.get_item() == 7)

        x = Node(9)
        n.set_next(x)
        assert(n.get_next() == x)
        assert(str(x) == "9")


class TestLinkedList(unittest.TestCase):

    def test_add(self):
        lst = LinkedList()

        lst.add(1)

        assert(lst.__repr__() == "1")

        n1 = Node(2)
        lst.add(n1)

        assert(lst.__repr__() == "1 2")

        n2 = Node(5)
        lst.add(n2)

        assert(lst.__repr__() == "1 2 5")
