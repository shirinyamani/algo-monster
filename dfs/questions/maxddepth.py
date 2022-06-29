# MaxDepth
# Question 1: Given a binary tree, find its maximum depth.
# note to go for return val approach of dfs, what do ya wanna return from children to parent after visiting them?
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1 # +1 for the root