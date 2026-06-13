# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def helper(node):
            if node is None:
                return (True,0)
            
            is_left_bal, left_h = helper(node.left)
            is_right_bal, right_h = helper(node.right)

            if not is_left_bal or not is_right_bal:
                return (False, None)
            elif abs(left_h - right_h) > 1:
                return (False, None)
            else:
                return (True, 1 + max(left_h, right_h))

        return helper(root)[0]