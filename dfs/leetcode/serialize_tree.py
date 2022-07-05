class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def serialize(root): #preorder traversal
    res = [] 
    def dfs(node):
        if not node:
            res.append("None") # serialize None as "None"
            return 
        
        res.append(str(node.val)) # serialize the node

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ", ".join(res)
    
    
def deserialize(data):
    vals = data.split(",")
    i = 0
    
    def dfs():
        if vals[i] == "N":
            i += 1
            return None
        node = TreeNode(int(vals[i]))
        i += 1
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()
