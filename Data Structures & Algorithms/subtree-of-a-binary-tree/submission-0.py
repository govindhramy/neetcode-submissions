# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        def is_equal(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val == q.val and is_equal(p.left,q.left) and is_equal(p.right,q.right)
        
        if is_equal(root, subRoot):
            return True
        elif root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False