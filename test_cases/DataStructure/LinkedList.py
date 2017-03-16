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

    def test_add_normal_and_size(self):
        lst = LinkedList()
        assert(lst.get_size() == 0)

        lst.add(1)
        assert(lst.__repr__() == "1")
        assert(lst.get_size() == 1)

        n1 = Node(2)
        lst.add(n1)
        assert(lst.__repr__() == "1 2")
        assert(lst.get_size() == 2)

        n2 = Node(5)
        lst.add(n2)
        assert(lst.__repr__() == "1 2 5")
        assert(lst.get_size() == 3)

    def test_add_index(self):
        lst = LinkedList()

        lst.add(1, 0)
        assert(lst.__repr__() == "1")
        assert(lst.get_size() == 1)

        lst.add(2, 0)
        assert(lst.__repr__() == "2 1")
        assert(lst.get_size() == 2)

        lst.add(3, 2)
        assert(lst.__repr__() == "2 1 3")
        assert(lst.get_size() == 3)

        lst.add(19, -1)
        assert(str(lst) == "2 1 3 19")

        lst.add(22, 2)
        assert(str(lst) == "2 1 22 3 19")

        self.assertRaises(ValueError, lst.add, 4, -2)
        self.assertRaises(ValueError, lst.add, 4, 6)

    def test_get(self):
        lst = LinkedList()
        lst.add(5)
        lst.add(3)
        lst.add(11)

        assert(lst.get(0) == 5)
        assert(lst.get(-1) == 11)
        assert(lst.get(2) == 11)

    def test_modify(self):
        lst = LinkedList()
        lst.add(5)
        lst.add(3)
        lst.add(11)
        lst.add(20)
        lst.add(30)

        lst.modify(50, 2)
        assert(lst.get(2) == 50)
        assert(str(lst) == "5 3 50 20 30")

        lst.modify(99, 0)
        assert(lst.get(0) == 99)
        assert(str(lst) == "99 3 50 20 30")

        lst.modify(70, -1)
        assert(lst.get(-1) == 70)
        assert(str(lst) == "99 3 50 20 70")

        lst.modify(60, 4)
        assert(lst.get(4) == 60)
        assert(str(lst) == "99 3 50 20 60")

    def test_remove(self):

        lst = LinkedList()
        self.assertRaises(ValueError, lst.remove, 2)

        lst.add(5)
        lst.add(3)
        lst.add(11)
        lst.add(20)
        lst.add(30)

        a = lst.remove(3)
        assert(a == 3)
        assert(str(lst) == "5 11 20 30")

        a = lst.remove(20)
        assert(a == 20)
        assert(str(lst) == "5 11 30")

        a = lst.remove(5)
        assert(a == 5)
        assert(str(lst) == "11 30")

        self.assertRaises(ValueError, lst.remove, 40)

    def test_remove_by_index(self):

        lst = LinkedList()
        self.assertRaises(ValueError, lst.remove_by_index, 0)

        lst.add(5)
        lst.add(3)
        lst.add(11)
        lst.add(20)
        lst.add(30)

        a = lst.remove_by_index(0)
        assert(a == 5)
        assert(str(lst) == "3 11 20 30")

        a = lst.remove_by_index(-1)
        assert(a == 30)
        assert(str(lst) == "3 11 20")

        a = lst.remove_by_index(2)
        assert(a == 20)
        assert(str(lst) == "3 11")

    def test_add_list(self):
        lsta = LinkedList()
        lsta.add_list(1, 2, 3, 4, 5)
        assert(str(lsta) == "1 2 3 4 5")

    def test_iterator(self):
        lst = LinkedList()
        lst.add_list(10, 23, 34, 45, 56)

        empty_list = []

        for x in lst:
            empty_list.append(str(x))
        result = " ".join(empty_list)
        assert(result == "10 23 34 45 56")

    def test_clear(self):
        lst = LinkedList()
        lst.clear()
        assert(lst.get_size() == 0)
        assert(str(lst) == "")

        lst.add(5)
        lst.add(3)
        lst.add(11)
        lst.add(20)
        lst.add(30)

        lst.clear()
        assert(lst.get_size() == 0)
        assert(str(lst) == "")
