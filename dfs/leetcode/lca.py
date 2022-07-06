#Idea is to find the separation point between p and q. n each time compare the value of the node with p and q. Pay attention to property of a BST

def LCA(root, p, q):
    if not root or not p or not q:
        return None

    elif root.val < p.val and root.val < q.val:
        return LCA(root.right, p, q)
    
    elif root.val > p.val and root.val > q.val:
        return LCA(root.left, p, q)

    else:
        return root



def lca(root, p, q):
    if not root or not q or not p:
        return None
    def dfs(root):
        if not root:
            return None
        if q.val < root.val and p.val< root.val:
            return dfs(root.left)

        elif p.val > root.val and q.val > root.val:
            return dfs(root.right)
        else: return root

    return dfs(root)