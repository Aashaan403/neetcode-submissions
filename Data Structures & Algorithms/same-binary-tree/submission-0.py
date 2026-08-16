# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traversalshit(node):
            if not node:
                return None
            
            left = traversalshit(node.left)
            right = traversalshit(node.right)
            
            return (node.val,left,right)
        
        checker = True
        if traversalshit(p) == traversalshit(q):
            return True
        else:
            return False