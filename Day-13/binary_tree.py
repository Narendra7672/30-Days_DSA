# Binary Tree Level Order Traversal:
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])   
    while queue:
        level_size = len(queue)
        current_level_values = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level_values.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)      
        result.append(current_level_values)       
    return result
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
output = level_order_traversal(root)
print("Level Order Traversal:", output)
