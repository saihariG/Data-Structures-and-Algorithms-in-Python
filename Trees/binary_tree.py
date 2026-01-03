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
        pass

    def iterative_preorder_traversal(self, root):
        pass

    def recursive_postorder_traversal(self, root):
        pass

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