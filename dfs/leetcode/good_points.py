#Question: return the number of good points in the tree; good points are points that are greater than or equal to the max value of the left subtree and the right subtree
#DFS is used to traverse the tree


def goodPoints(root):

    def dfs(node, maxVal):
        if not node:
            return 0

        count = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)

        count += dfs(node.left, maxVal)
        count += dfs(node.right, maxVal)

        return count

    return dfs(root,root.val)