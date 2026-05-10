# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    cnt = 0
    ans = -1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.cnt +=1
            if self.cnt == k:
                self.ans = node.val
            inorder(node.right)

            
        # left -> root -> right
        inorder(root)
        return self.ans