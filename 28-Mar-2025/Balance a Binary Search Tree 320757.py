# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        def balance(start, end):
            if start > end:
                return None
            mid = (start + end) // 2 
            node = TreeNode(values[mid])
            node.left = balance(start, mid - 1)
            node.right = balance(mid + 1, end)
            return node

        values = []
        inorder(root)
        return balance(0, len(values) - 1)
