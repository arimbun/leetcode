from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # base case
        if len(nums) <= 1:
            return 0

        # any other cases
        s_nums = sorted(nums)
        count = 0
        a = 0
        b = len(s_nums)-1
        while a < b:
            sumz = s_nums[a]+s_nums[b]
            if sumz == k:
                count += 1
                a+=1
                b-=1
            elif sumz < k:
                a+=1
            else:
                b-=1

        return count


sol = Solution()
print(sol.maxOperations(nums = [1,2,3,4], k = 5))
print(sol.maxOperations(nums = [3,1,3,4,3], k = 6))
