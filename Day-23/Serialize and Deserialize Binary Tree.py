# Serialize and Deserialize Binary Tree:
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root: TreeNode) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
serialized_data = codec.serialize(root)
print(serialized_data)

deserialized_root = codec.deserialize(serialized_data)
print(codec.serialize(deserialized_root))
