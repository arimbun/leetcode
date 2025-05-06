from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Solves 3 sum problem using two pointer approach"""

        # array must be sorted
        sorted_nums = sorted(nums)

        # store result in set (to prevent duplicates)
        result = set()

        # start with the leftmost element
        for a in range(len(sorted_nums)-2):
            b = a+1                         # 2nd pointer = 1st pointer + 1
            c = len(sorted_nums)-1          # 3rd pointer starts from the last element

            while b < c:
                i = sorted_nums[a]
                j = sorted_nums[b]
                k = sorted_nums[c]

                if i+j+k == 0:
                    # if sum equals target, store result and move both pointers
                    result.add(tuple(sorted( (i,j,k) )))        # sort the tuple (i,j,k) to remove duplicates
                    b += 1
                    c -= 1
                elif i+j+k < 0:
                    # at this point the sum is less than target, so it is pointless to move 2nd pointer further left,
                    # instead move 1st pointer to the right (to get larger number)
                    b += 1
                else:
                    # sum does not equal target (yet), so move 2nd pointer further left until either
                    # sum equals target or sum goes below target
                    c -= 1

        # convert result to list(list(int))
        return [list(r) for r in result]

nums = [-1,0,1,2,-1,-4]
sol = Solution()
[print(i) for i in sol.threeSum(nums)]
