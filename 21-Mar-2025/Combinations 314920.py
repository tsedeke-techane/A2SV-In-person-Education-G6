# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start):
            if len(path) == k:
                ans.append(path[:])
                return 
            if start > n:
                return
            # include
            path.append(start)
            backtrack(start + 1)

            # not include
            path.pop()
            backtrack(start + 1)

        ans = []
        path = []
        backtrack(1)
        return ans
                
            