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
    data = data.split(", ") #['s', 'h', 'r']
    def dfs():
        val = data.pop(0)  #element pop for creating the nodes
        if val == "None":
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()
