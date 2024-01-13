from linkednode import LinkedNode


class LinkedList:

    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0

    def __str__(self):
        if self._front is None:
            return 'LinkedList([])'
        else:
            return 'LinkedList([' + str(self._front) + '])'

    def __len__(self):
        """ 
        Rather than traversing the list from front to end, it is better to have an attribute _size
        that is updated every time we add or remove an element.
        The code below shows you how to traverse a linked list, from start to end. 
        To traverse the list, we need to use a local variable <currentnode> to move along the list, 
        we must not change/move the pointer _front.
            count = 0
            currentnode = self._front
            while currentnode is not None:
                count += 1
                currentnode = currentnode._next

        """
        return self._size

    def append(self, value):
        newnode = LinkedNode(value)
        if self._front is None:
            self._front = newnode
            self._tail = newnode
        else:
            self._tail.tail = newnode
            self._tail = newnode

        self._size += 1

    def pop(self):
        if self.isempty():
            raise IndexError('The list is empty.')

        front_node = self._front
        self._front = self._front.tail
        front_node.tail = None
        self._size -= 1
        return front_node.data

    def clear(self):
        self.__init__()

    def index(self, value, start=0, stop=2147483647):
        i = 0
        current = self._front
        while current:
            if start <= i < stop and current._data == value:
                return i
            i += 1
            current = current._next
        raise ValueError(f"{value} is not in list")

    def insert(self, index, object):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        new_node = LinkedNode(object)
        if index == 0:
            new_node._next = self._front
            self._front = new_node
        else:
            i = 0
            current = self._front
            while i < index - 1 and current:
                i += 1
                current = current._next
            new_node._next = current._next
            current._next = new_node
        self._size += 1

    def remove(self, value):
        if self._front is None:
            raise ValueError("List is empty")
        if self._front._data == value:
            self._front = self._front._next
        else:
            current = self._front
            prev = None
            while current:
                if current._data == value:
                    prev._next = current._next
                    self._size -= 1
                    return
                prev = current
                current = current._next
            raise ValueError(f"{value} is not in list")

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        i = 0
        current = self._front
        while i < index and current:
            i += 1
            current = current._next
        if current is None:
            raise IndexError("Index out of range")
        return current._data

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        i = 0
        current = self._front
        while i < index and current:
            i += 1
            current = current._next
        if current is None:
            raise IndexError("Index out of range")
        current._data = value
