from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        highest = max(candies)

        for c in candies:
            can_have = c + extraCandies
            result.append(can_have >= highest)

        return result

sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))
