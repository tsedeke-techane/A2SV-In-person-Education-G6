# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        for pile in piles:
            heappush(max_heap, -pile)

        for _ in range(k):
            largest = -heappop(max_heap)
            reduced = (largest + 1) // 2

            heappush(max_heap, -reduced)

        return -sum(max_heap)
        
