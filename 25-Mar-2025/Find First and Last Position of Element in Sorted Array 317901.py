# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            left = 0
            right = len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return first

        def findLast():
            left = 0
            right = len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1
            return last

        return [findFirst(), findLast()]
                




            
