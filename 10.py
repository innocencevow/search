from collections import deque  

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if root is None:   
       return [] 
    result = []
    queue = deque([root])           
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()      
            level.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(level)

    return result


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(levelOrder(root))
    #  [[3], [9, 20], [15, 7]]

    print(levelOrder(None))