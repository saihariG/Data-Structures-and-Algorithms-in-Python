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


    # Algorithm for displaying the list
    def print_linked_list(self):
        current = self.head

        while current is not None:
            print(f"{current.data} --> ")
            current = current.next

        print("None")

    # Algorithm to find the middle node
    # 1. create nodes Slow and Fast and point them to head
    # 2. Traverse slow and fast until fast and its next is not null
    # 3. After traversing, print slow 's data if not null
    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        if slow is not None:
            print(f"Middle node: {slow.data} --> ")


    # Algorithm to delete a given node
    # 1. Create two nodes current and temp, while current pointing to head
    # 2. if current_node's data equals Key, then move the head to current's next (deleting)
    # 3. Traverse the list until the key is not found, while tracking the temp with current
    # 4. If current is null, we are at the end of the list (Key not found), So return
    # 5. When the Key is found, make temp's next point to current's next
    def delete_node(self, key):
        current_node = self.head
        temp = None

        if current_node.data == key:
            self.head = current_node.next
            return

        while current_node is not None and current_node.data is not key:
            temp = current_node
            current_node = current_node.next

        # Traversed the entire list
        if current_node is None:
            return

        # Key found
        temp.next = current_node.next


    # Algorithm to reverse a linked list
    # 1. create nodes current and prev while current points to head
    # 2. Temporarily store the next_node (head's next)
    # 3. Reverse the link
    # 4. Move previous and current one step ahead
    # 5. Update the head to the new first node which is previous
    def reverse_list(self):
        current = self.head
        previous = None

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # Algorithm to detect a loop
    # 1. Create two nodes slow and fast pointing to head
    # 2. Traverse slow and fast, while fast's next is not None
    # 3. if Slow equals fast, then there is a loop
    # 4. There is no loop after entire traversal, so return false
    def detect_loop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    # Algorithm to detect cycle node (returns the node where cycle begins)
    # 1. Create two nodes slow and fast pointing to head
    # 2. Traverse slow and fast, while fast and it's next is not None
    # 3. if slow equals fast, create a current node pointing to head and traverse it until slow
    # 4. return the slow node (where exactly cycle begins)
    # 5. return None
    def detect_cycle_node(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                current = self.head

                while current != slow:
                    current = current.next
                    slow = slow.next
                return slow

        return None