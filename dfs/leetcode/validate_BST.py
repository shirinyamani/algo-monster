def validateBST(root):
    def valid(node, left, right):
        if not node:
            return True
        if not (node.val > left and node.val < right):
            return False

        return (valid(node.left, left, node.val) and
                valid(node.right, node.val, right))

    return valid(root, float('-inf'), float('inf'))