class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class CodeC:

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
    
    
    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        
        def dfs():
            if vals[self.i] == "Null":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
