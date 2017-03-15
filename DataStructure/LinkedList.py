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


# Normal Singly Linked List
class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def add_list(self, *args):
        for value in (args):
            self.add(value)

    def add(self, item, index=-1):
        self._check_index(index)

        current = self.head
        if current:
            if index == -1:  # Default case: Add to the tail
                while current.get_next():
                    current = current.get_next()
                current.set_next(Node(item))
            else:
                prev = current  # When index is given
                for x in range(0, index):
                    prev = current
                    current = current.get_next()
                n = Node(item)
                if self.head == current:  # Check if list only contains an element
                    n.set_next(current)
                    self.head = n
                else:
                    prev.set_next(n)
                    n.set_next(current)
        else:
            self.head = Node(item)
        self.size += 1

    def remove(self, item):
        if self.size == 0:
            raise ValueError("Can't delete an empty list")
        is_deleted = False
        curr = self.head
        prev = curr
        while curr:
            if curr.get_item() == item:  # Desired item found
                if self.head == curr:  # If the item is the head
                    self.head = curr.get_next()
                else:
                    n = curr.get_next()
                    prev.set_next(n)
                is_deleted = True
                self.size -= 1
                break
            else:
                prev = curr
                curr = curr.get_next()
        if not is_deleted:
            raise ValueError("Item is not inside the list")

    def remove_by_index(self, index):
        self._check_index(index)
        if self.size == 0:
            raise ValueError("Can't delete an empty list")

        if index == -1:
            index = self.size - 1  # Get the last element
        current = self.head
        prev = current
        for i in range(0, index):
            prev = current
            current = current.get_next()
        if self.head == current:  # If the item is the head
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())
        self.size -= 1

    def get_size(self):
        return self.size

    def get(self, index):
        current = self._get_node(index)
        return current.get_item()

    def _get_node(self, index):
        self._check_index(index)
        if index == -1:
            index = self.size - 1  # Get the last element
        current = self.head
        for i in range(0, index):
            current = current.get_next()
        return current

    def modify(self, item, index):
        current = self._get_node(index)
        current.set_item(item)
        return current.get_item()

    def _is_index_valid(self, index):
        return index > self.size

    def _is_index_positive(self, index):
        return index < -1

    def _check_index(self, index):
        if self._is_index_valid(index):
            raise ValueError("Index is larger than the list size")

        if self._is_index_positive(index):
            raise ValueError(
                "Index must be positive")

    def __repr__(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(str(curr.get_item()))
            curr = curr.get_next()
        return " ".join(lst)

    def __iter__(self):
        current = self.head
        while current:
            yield current.get_item()
            current = current.get_next()
