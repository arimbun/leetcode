from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # setup binary search using pointers
        a = 0
        b = 2 * max(candies)

        candies_per_child = int( (a+b)/2 )
        candies_per_child_prev = -1
        while candies_per_child != candies_per_child_prev:
            if candies_per_child == 0:
                return 0

            # given `candies_per_child` allocation per child,
            # how many children gets a pile each?
            kk = 0
            for cd in candies:
                kk += int(cd/candies_per_child)

            if kk < k:
                # too few children gets a pile - try reducing allocation
                b = candies_per_child
            else:
                # too many children gets a pile - try increasing allocation
                a = candies_per_child

            candies_per_child_prev = candies_per_child
            candies_per_child = int( (a+b)/2 )

        return candies_per_child

sol = Solution()
print( sol.maximumCandies(candies = [5,8,6], k = 3) ) # 5
print( sol.maximumCandies(candies = [2,5], k = 11) ) # 0
