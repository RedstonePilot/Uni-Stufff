from linkednode import LinkedNode


class LinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        self._top = LinkedNode(value, self._top)
        self._size += 1

    def __str__(self):
        nodes = []
        current = self._top
        while current:
            nodes.append(str(current._data))
            current = current._next
        return 'LinkedStack([' + ', '.join(nodes) + '])'

    def pop(self):
        if not self._top:
            raise ValueError
        popped_value = self._top._data
        self._top = self._top._next
        self._size -= 1
        return popped_value

    def peek(self):
        if self._top == None:
            return None
        return self._top._data

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0
