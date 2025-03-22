# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub(idx):
            if idx == len(nums):
                ans.append(subset[:])  
                return 

            # include
            subset.append(nums[idx])
            sub(idx + 1)

            # not include
            subset.pop()
            sub(idx + 1)                                   

        ans = []
        subset = []
        sub(0)
        return ans