# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]): 
        
        nums = [0] + nums
        self.nums = nums
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)