class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.leftSize = 0
    
        def insert(root, val): # O(log n) # BC insertion in arr is O(n)
            if root is None:
                return Node(val)

            elif val < root.val:
                    root.left = insert(root.left, val)
                    root.leftSize += 1
            else:
                root.right = insert(root.right, val)

            return root

        def get_rank(root, x):
            if root.val == x:
                return root.leftSize

            elif x < root.val:
                if root.left is None:
                    return -1
                else:
                    return get_rank(root.left, x)
            else:
                if root.right is None:
                    return -1
                else:
                    return root.leftSize + 1 + get_rank(root.right, x)
        






