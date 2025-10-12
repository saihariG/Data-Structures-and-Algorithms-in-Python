class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Algo to insert node at beginning
    def insert_node_at_first(self, data):
        new_node = ListNode(data)

        # if the list is not empty
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        # if list is empty
        self.head = new_node