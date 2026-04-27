class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete_node(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def insert_between(self, value, prev_value, next_value):
        new_node = Node(value)
        current = self.head
        while current:
            if current.value == prev_value and current.next and current.next.value == next_value:
                new_node.prev = current
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                return
            current = current.next