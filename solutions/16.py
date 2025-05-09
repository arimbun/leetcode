from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)          # numbers array must be sorted
        best_delta = float('inf')
        result = []

        # 1st pointer starts with the leftmost element
        for a in range(len(sorted_nums)-2):
            b = a+1                         # 2nd pointer = 1st pointer + 1
            c = len(sorted_nums)-1          # 3rd pointer starts from the last element

            while b < c:
                i = sorted_nums[a]
                j = sorted_nums[b]
                k = sorted_nums[c]
                ijk = i+j+k

                # if delta is lower than before, save this as best result
                delta = abs(target-ijk)
                if delta < best_delta:
                    result = [i,j,k]
                    best_delta = delta

                if ijk >= target:
                    # if sum is larger than target then move 3rd pointer left
                    # (to smaller number) to try and reduce delta
                    c -= 1
                else:
                    # if sum is smaller than target then move 2nd pointer right
                    # (to larger number) to try and reduce delta
                    b += 1

        return sum(result)

nums = [-1,2,1,-4]
target = 1

nums1 = [0,0,0]
target1 = 1

nums2 = [1,1,1,1]
target2 = 0

nums3 = [-84,92,26,19,-7,9,42,-51,8,30,-100,-13,-38]
target3 = 78

sol = Solution()
print(sol.threeSumClosest(nums, target))    # 2
print(sol.threeSumClosest(nums1, target1))  # 0
print(sol.threeSumClosest(nums2, target2))  # 3
print(sol.threeSumClosest(nums3, target3))  # 77
