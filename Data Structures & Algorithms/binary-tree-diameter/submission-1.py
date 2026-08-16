# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res =0
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)

            self.res = max(self.res,left+right)#enthukonda ivide left +right +1 illathe ennalle
            #onnu aalochich nokiye length alle 5 nodes adipichu bekanel aanel polum athinte idel ulla length verum 4 aa (5 -1)

            return 1+max(left,right)

        height(root)
        return self.res


        

        