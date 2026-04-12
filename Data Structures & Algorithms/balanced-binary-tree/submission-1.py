# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfsHeight(self, node: Optional[TreeNode]) -> int:
            if not node: return 0

            leftH = self.dfsHeight(node.left)
            if leftH == -1: return -1
            rightH = self.dfsHeight(node.right)
            if rightH == -1: return -1

            if abs(leftH - rightH) > 1: return -1

            return 1 + max(leftH, rightH)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfsHeight(root) != -1