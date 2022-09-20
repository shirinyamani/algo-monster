from collections import deque
def bfs(root):
    queue = deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)












if __name__ == "__main__":
    bfs([1,2,3,4,5,6,7])