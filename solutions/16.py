from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # numbers array must be sorted
        sorted_nums = sorted(nums)

        # iunfinit
        best_delta = float('inf')
        result = []

        # 1st pointer starts with the leftmost element
        for a in range(len(sorted_nums)-2):
            b = a+1                         # 2nd pointer = 1st pointer + 1
            c = len(sorted_nums)-1          # 3rd pointer starts from the last element

            # this stores the previous delta we found during iteration
            delta_prev = float('inf')
            while b < c:
                i = sorted_nums[a]
                j = sorted_nums[b]
                k = sorted_nums[c]
                ijk = i+j+k
                delta = abs(target-ijk)

                if delta < best_delta:
                    # if delta is closer to target than best delta, then set it
                    # as the best delta and store [i,j,k] as the new best result
                    best_delta = delta
                    result = [i, j, k]
                    delta_prev = delta
                elif delta <= delta_prev:
                    # if delta is getting smaller then continue iterating;
                    # we may be able to find an even better delta
                    c -= 1
                    delta_prev = delta
                elif delta > delta_prev:
                    # if delta is getting larger then it is pointless to keep
                    # iterating 3rd pointer, instead it is time to advance 2nd
                    # pointer
                    b += 1
                    c = len(sorted_nums)-1
                    delta_prev = float('inf')

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
print(sol.threeSumClosest(nums, target))
print(sol.threeSumClosest(nums1, target1))
print(sol.threeSumClosest(nums2, target2))
print(sol.threeSumClosest(nums3, target3))  # 77
