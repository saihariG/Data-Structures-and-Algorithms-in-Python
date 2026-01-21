class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
A Binary Search Tree is a binary tree with an ordering rule:

Left subtree -> values less than the node
Right subtree -> values greater than the node

"""

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.data = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)

        return root
    

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.data == key:
            return root
        
        if key < root.data:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)
        
    
    """
    Deleting a node:

    1. Leaf node
    2. Node with 1 child
    3. Node with 2 children (Replace the node with:)
        - Inorder Predecessor (largest in left subtree)
        - Inorder successor (smallest in right subtree)

    """

    def delete(self, key):
        self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        
        if key < root.data:
            root.left = self._delete(root.left, key)
        elif key > root.data:
            root.right = self._delete(root.right, key)
        # If key is same as root's data, it needs to be deleted
        else:

            # case 1 & 2: node with a single child
            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left
            
            # node with 2 children: Get the inorder successor
            root.data = self.get_min_in_right_subtree(root.right)

            # Delete the inorder successor
            root.right = self._delete(root.right, root.data)

        return root
    
    def get_min_in_right_subtree(root):
        min = root.data 

        while root.left:
            min = root.left.data
            root = root.left

        return min
    
if __name__ == "__main__":
    bst = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("Search 40:", bst.search(40) is not None)

    bst.delete(50)