from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # initialise two pointers
        k1 = 0
        k2 = max(piles)

        # any other case
        k = math.ceil((k1+k2)/2)  # initial eating speed = 1st pointer
        k_prev = -1
        h_total = float('inf')
        while True:
            h_total = 0
            for pi in piles:
                h_pi = int(math.ceil(pi/k))
                h_total += h_pi

            if k_prev == k:
                return k
            elif h_total <= h: # eat too fast
                k2 = k
            else: # eat too slow
                k1 = k

            # reset eating speed
            k_prev = k
            k = math.ceil((k1+k2)/2)

sol = Solution()
print("-- k:", sol.minEatingSpeed(piles = [3,6,7,11], h = 8)) # 4
print("-- k:", sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5)) # 30
print("-- k:", sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6)) # 23
print("-- k:", sol.minEatingSpeed(piles = [312884470], h = 312884469)) # 2
print("-- k:", sol.minEatingSpeed(piles = [312884470], h = 968709470)) # 1
print("-- k:", sol.minEatingSpeed(piles = [1,1,1,999999999], h = 10)) # 142857143
