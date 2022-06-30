#Idea is to find the separation point between p and q. n each time compare the value of the node with p and q. 

def LCA(root, p, q):
    if not root or not p or not q:
        return None

    elif root.val < p.val and root.val < q.val:
        return LCA(root.right, p, q)
    
    elif root.val > p.val and root.val > q.val:
        return LCA(root.left, p, q)

    else:
        return root