# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxPos = 0
        minNeg = 0
        ans = 0
        for num in nums:
            maxPos = max(0 , maxPos   + num)
            minNeg = min(0 , minNeg   + num)
           
            ans = max(abs(minNeg) , maxPos , ans)
            
        return ans

