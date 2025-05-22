from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        # D[l] will be the smallest element at which an increasing subsequence of length 'l' ends
        D = [float('inf')] * 4
        D[0] = float('-inf')
        for i in range(len(nums)):
            for l in range(1, len(D)):
                if nums[i] > D[l-1]:
                    D[l] = min(nums[i], D[l])

        return D[3] < float('inf')

sol = Solution()
print(sol.increasingTriplet(nums = [1,2,3,4,5]))
print(sol.increasingTriplet(nums = [5,4,3,2,1]))
print(sol.increasingTriplet(nums = [2,1,5,0,4,6]))
print(sol.increasingTriplet(nums = [6,7,1,2]))   # false
