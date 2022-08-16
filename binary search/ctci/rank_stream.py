class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.leftSize = 0
    
    def insert(root, val):
        if root is None:
            return Node(val)

        elif val < root.val:
                root.left = insert(root.left, val)
                root.leftSize += 1
        else:
            root.right = insert(root.right, val)

        return root





