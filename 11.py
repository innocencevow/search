class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    result = []
    if root is None:
        return result

    queue = [root]

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop(0)      

            if i == level_size - 1:
                result.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return result


if __name__ == "__main__":
   
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    print(rightSideView(root))   # [1, 3, 4]
    
    print(rightSideView(TreeNode(1)))   # [1]

    print(rightSideView(None))   # []