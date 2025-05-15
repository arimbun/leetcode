from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # base case
        if len(nums) <= 1:
            return [[nums[0]]]

        # normal case
        result = []
        all_i = set()
        for i in nums:
            if i not in all_i:
                result_2 = nums.copy()
                result_2.remove(i)
                for lst in self.permuteUnique(result_2):
                    result.append([i]+lst)
                all_i.add(i)

        return result

sol = Solution()
print(sol.permuteUnique( [1,2,3] ))
print(sol.permuteUnique( [1,1,2] ))
