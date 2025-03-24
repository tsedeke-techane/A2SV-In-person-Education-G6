# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        def binary(path):
            if len(path) == n:
                ans.append(path)
                return
            
            binary(path + '1')

            if not path or path[-1] == '1':
                binary(path + '0')

        ans = []
        binary('')
        return ans    