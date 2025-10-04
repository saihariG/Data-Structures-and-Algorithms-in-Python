class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    #  Algo to insert node at beginning of the list
    #   1. create a new node and pass the data to be inserted
    #   2. now make its next to point head
    #   3. update head
    def insert_at_first(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    # Algo to insert node at the end of the list
    # 1. Create a new node
    # 2. If the list is empty, insert node at the head and return
    # 3. Create a current node pointing to the head and traverse until it's next is not null
    # 4. Then, insert the new_node to current's next
    def insert_at_last(self, data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node


    # Algorithm for counting length
    #   1. have a counter and initialize to zero
    #   2. create a new node current and initialize to head
    #   3. Traverse till the end of the list
    #   4. and increase the counter
    def count_and_print_length(self):
        n = 0

        current = self.head
        while current is not None:
            current = current.next
            n += 1

        print(f"Length of linked list: {n}")

    # Algorithm for searching a node
    #   1. If head is null, then there list is empty
    #   2. create a current node and initialize to head
    #   2. initialize a counter variable to zero
    #   3. traverse until current is not null
    #   4. if data found return else traverse to next element and increase the counter
    #   5. If the list is completely traversed, print Key not found
    def search_node(self, key):
        if self.head is None:
            print("Search key not found")

        current = self.head
        count = 0

        while current is not None:
            if current.data == key:
                print(f"Found key: {key} at index: {count}")
                return

            current = current.next
            count += 1

        print("Key not found")