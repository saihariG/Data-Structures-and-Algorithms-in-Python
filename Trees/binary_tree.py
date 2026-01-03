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

    def iterative_inorder_traversal(self, root):
        pass 

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

    def iterative_postorder_traversal(self, root):
        pass 

    def level_order_traversal(self, root):
        pass 

    def height_of_binary_tree(self, root):
        pass

if __name__ == '__main__':
    bt = BinaryTree() 

    root1 = create_binary_tree()
    root2 = create_binary_tree_2()
 
    bt.recursive_inorder_traversal(root1)
    bt.recursive_preorder_traversal(root1)
    bt.recursive_postorder_traversal(root1)