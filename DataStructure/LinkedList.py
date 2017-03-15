class Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None

    def set_next(self, node):
        self.next = node
        return self

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_item(self, item):
        self.item = item
        return self

    def __repr__(self):
        return str(self.item)


class LinkedList(object):

    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        if current:
            while current.get_next():
                current = current.get_next()
            current.set_next(Node(item))
        else:
            self.head = Node(item)

    def __repr__(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(str(curr.get_item()))
            curr = curr.get_next()
        return " ".join(lst)
