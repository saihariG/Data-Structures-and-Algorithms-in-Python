class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Algo to insert node at beginning
    def insert_node_at_first(self, data):
        new_node = ListNode(data)

        # if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # if the list is not empty
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Algo to insert node at end
    def insert_node_at_end(self, data):
        new_node = ListNode(data)

        # if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # we reached the end of the list
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # Algo to delete node at first
    def delete_node_at_first(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        current = self.head

        current.next.prev = None
        self.head = current.next
        current.next = None

    # Algo to delete node at end:
    def delete_node_at_end(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        current = self.tail

        current.prev.next = None
        self.tail = current.prev
        current.prev = None