from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # initialise window sliders
        a=b=0

        for b in range(len(nums)):
            # if we encounter a 0 the we decrement k
            if nums[b] == 0:
                k-=1

            # if k < 0 then we have used up all available k,
            # we need to slide 'a' forward
            if k < 0:
                # if 'a' sits on zero then we recover k that was used to
                # to turn it to one
                if nums[a] == 0:
                    k+=1
                a+=1

        # this is the final window size
        return b-a+1


sol = Solution()
print( sol.longestOnes(nums = [0], k = 0) ) # 0
print( sol.longestOnes(nums = [1], k = 0) ) # 1
print( sol.longestOnes(nums = [0], k = 1) ) # 1
print( sol.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2) ) # 6
print( sol.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3) ) # 10
