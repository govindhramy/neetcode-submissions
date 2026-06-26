# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0

        def dfs(node, greatest_so_far):
            nonlocal goodNodes

            if node is None:
                return

            if greatest_so_far <= node.val:
                goodNodes += 1

            greatest_so_far = max(greatest_so_far, node.val)
            dfs(node.left, greatest_so_far)
            dfs(node.right, greatest_so_far)
        
        dfs(root, -999)
        return goodNodes
        