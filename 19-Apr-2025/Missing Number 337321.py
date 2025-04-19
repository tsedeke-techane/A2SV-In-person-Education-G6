# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n + 1):
            total += i

        actual = sum(nums)
        return total - actual
