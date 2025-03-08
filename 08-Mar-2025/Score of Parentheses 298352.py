# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  

        for ch in s:
            if ch == '(':
                stack.append(0)  
            else:
                mul = stack.pop()  
                stack[-1] += max(2 * mul, 1)

        return stack.pop()
