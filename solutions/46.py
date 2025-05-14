from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case
        if len(nums) <= 1:
            return [[nums[0]]]

        # normal case
        result = []
        for i in nums:
            result_2 = [x for x in nums if x != i]
            for lst in self.permute(result_2):
                result.append([i]+lst)
        return result

sol = Solution()
print(sol.permute( [1,2,3] ))
print(sol.permute( [0,1] ))
print(sol.permute( [1] ))
