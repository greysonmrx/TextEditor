class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.start = Node('')
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def top(self):
        if (self.is_empty()):
            return print('The stack is empty')

        return self.start.next.value

    def push(self, value):
        node = Node(value)

        node.next = self.start.next

        self.start.next = node
        self.size += 1

    def pop(self):
        if (self.is_empty()):
            return print('The stack is empty')

        remove = self.start.next

        self.start.next = self.start.next.next
        self.size -= 1

        return remove.value

    def clear(self):
        while(self.size > 0):
            self.pop()
