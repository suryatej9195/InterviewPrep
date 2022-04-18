class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        output = []
        if not root:
            return root
        self.inorder(root, output, k)
        return output[-1]
    
    def inorder(self, node, output, k):
        if not node:
            return None
        self.inorder(node.left, output, k)
        if len(output) == k:
            return
        else:
            output.append(node.val)
        self.inorder(node.right, output, k)