# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def fun(node):
            if node is None:
                return 0, 0

            left_sum, left_count = fun(node.left)
            right_sum, right_count = fun(node.right)

            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1

            if subtree_sum // subtree_count == node.val:
                nonlocal count_node
                count_node += 1

            return subtree_sum, subtree_count
        count_node = 0
        fun(root)
        return count_node