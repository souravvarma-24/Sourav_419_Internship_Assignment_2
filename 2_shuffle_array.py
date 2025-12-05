from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mixed = []
        left = nums[:n]
        right = nums[n:]

        for i in range(n):
            mixed.append(left[i])
            mixed.append(right[i])

        return mixed


sol = Solution()
print(sol.shuffle([2, 5, 1, 3, 4, 7], 3))
