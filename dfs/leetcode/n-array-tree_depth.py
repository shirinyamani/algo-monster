#Question: maximum depth on n-array tree

def maxDepth(root):
    if not root:
        return 0
    if root.children:
        return max(maxDepth(child)+1 for child in root.children)
    return 1

