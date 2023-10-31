    class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, node, data):
        if node is None:
            return

        new_node = Node(data)
        new_node.next = node.next
        new_node.prev = node

        if node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node

        node.next = new_node

    def delete(self, node):
        if node is None:
            return

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
