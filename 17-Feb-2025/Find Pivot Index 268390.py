# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = [0] + nums
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        for pivot_index in range(1,len(nums)):
            if nums[pivot_index - 1] == nums[- 1] - nums[pivot_index]:
                return pivot_index - 1

        return -1
