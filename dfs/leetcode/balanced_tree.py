# Question: Given a binary tree, determine if it is height-balanced.
#NOTE: check for every n each node is balanced or not

def balanced(root):
    def dfs(root):
        if not root:
            return [True,0] # [is_balanced, height]
        
        left, right = dfs(root.left), dfs(root.right)
        diff = abs(left[1] - right[1])

        balanced = True if (left[0] and right[0] and diff <= 1) else False

        return (balanced, max(left[1], right[1]) + 1) #`max(left[1], right[1]) + 1` is the height of the tree
    return dfs(root)[0]





    