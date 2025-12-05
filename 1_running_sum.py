from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        output = []

        for num in nums:
            total += num
            output.append(total)

        return output


sol = Solution()
sol.runningSum([1,2,3,4])
