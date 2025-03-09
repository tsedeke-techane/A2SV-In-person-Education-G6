# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        count = 0
        for charr in s:
            if count == 0:
                ans += 1

            if charr == "R":
                count += 1
            else:
                count -= 1
                
        return ans