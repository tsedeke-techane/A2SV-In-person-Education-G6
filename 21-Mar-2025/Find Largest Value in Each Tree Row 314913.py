# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        que = deque([root])
        if not root: return []
        while que:
            max_value = float('-inf')
            for _ in range(len(que)):
                node = que.popleft()
                max_value = max(max_value, node.val)

                if node.left:
                    que.append(node.left)
                    

                if node.right:
                    que.append(node.right)
                
            ans.append(max_value)
        
        return ans