# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.ans

    def helper(self, node):
        
        if node.left:
            left_length = 1 + self.helper(node.left)
        else:
            left_length = 0

        if node.right:
            right_length = 1 + self.helper(node.right)
        else:
            right_length = 0

        self.ans = max(self.ans, left_length + right_length)
        
        return max(left_length, right_length)
        