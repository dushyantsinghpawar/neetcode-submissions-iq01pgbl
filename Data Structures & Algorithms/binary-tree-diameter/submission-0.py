# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfsHeight(self, node: Optional[Treenode]) -> int:
        if not node: return 0

        leftH = self.dfsHeight(node.left)
        rightH = self.dfsHeight(node.right)

        self.diameter = max(self.diameter, leftH + rightH)

        return 1 + max(leftH, rightH)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0
        self.dfsHeight(root)
        
        return self.diameter