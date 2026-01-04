from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_binary_tree():
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    root = first
    root.left = second
    root.right = third

    second.left = fourth
    second.right = fifth

    return root


def create_binary_tree_2():
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seven = Node(7)

    root = first
    root.left = second
    root.right = third

    second.left = fourth
    second.right = fifth

    third.left = sixth
    third.right = seven

    return root

class BinaryTree:
    def recursive_inorder_traversal(self, root):
        if root == None:
            return 
        
        self.recursive_inorder_traversal(root.left)
        print(root.data)
        self.recursive_inorder_traversal(root.right)

    # Left -> Root -> Right, So go as left as possible
    # Push nodes into the stack
    # When we can't go left:
        #  pop from the stack
        #  Process the node
        #  Move to the right subtree
    def iterative_inorder_traversal(self, root):
        if root == None:
            return

        stack = []
        current = root

        while stack or current:
            if current:
                stack.push(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.data + " ")
                # visit the right subtree
                current = current.right


    def recursive_preorder_traversal(self, root):
        if root is None:
            return
        
        print(root.data)
        self.recursive_preorder_traversal(root.left)
        self.recursive_preorder_traversal(root.right)

    # If root is None, return
    # Define a stack and push the root node
    # while stack is not empty,
        # pop and print the node's data
        # push the node's right, so left is processed first
        # push the node's left next
    def iterative_preorder_traversal(self, root):
        if root is None:
            return
        
        stack = [root]

        while stack:
            temp_node = stack.pop()
            print(temp_node.data + " ")

            if temp_node.right:
                stack.append(temp_node.right)
            
            if temp_node.left:
                stack.append(temp_node.left)


    def recursive_postorder_traversal(self, root):
        if root is None:
            return
        
        self.recursive_postorder_traversal(root.left)
        self.recursive_postorder_traversal(root.right)
        print(root.data)

    # Idea: Root is processed last, Left -> Right -> Root
    # 1. First stack -> simulate preorder
    # 2. Second stack -> reverse the order to get Left -> Right -> Root
    def iterative_postorder_traversal(self, root):
        if root is None:
            return
        
        stack1 = [root]
        stack2 = []
        
        while stack1:
            temp_node = stack1.pop()
            stack2.append(temp_node)

            if temp_node.left:
                temp_node = temp_node.left

            if temp_node.right:
                temp_node = temp_node.right
            
        while stack2:
            print(stack2.pop().data)

    # Idea: Use a queue (FIFO)
    # start with the root 
    # Process nodes in the order they were inserted
    def level_order_traversal(self, root):
        if root is None:
            return
        
        queue = deque([root])

        while queue:
            temp_node = queue.popleft()
            print(temp_node.data)

            if temp_node.left:
                queue.append(temp_node.left)

            if temp_node.right:
                queue.append(temp_node.right) 


    def height_of_binary_tree(self, root):
        pass

if __name__ == '__main__':
    bt = BinaryTree() 

    root1 = create_binary_tree()
    root2 = create_binary_tree_2()
 
    bt.recursive_inorder_traversal(root1)
    bt.recursive_preorder_traversal(root1)
    bt.recursive_postorder_traversal(root1)

    bt.iterative_inorder_traversal(root2)
    bt.iterative_preorder_traversal(root2)
    bt.iterative_postorder_traversal(root2)

    bt.level_order_traversal(root1)