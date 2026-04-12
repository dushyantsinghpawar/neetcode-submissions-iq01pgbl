# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, node: Optional[TreeNode]) -> list:
        ans = []
        def preorder(n: Optional[TreeNode]):    
            if not n:
                ans.append(None)
                return            
            ans.append(n.val)
            preorder(n.left)
            preorder(n.right)
        
        preorder(node)
        return ans
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.preorderTraversal(p) == self.preorderTraversal(q)