from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s_nums = sorted(nums)
        # print("s_nums:",s_nums)

        result = []
        for a in range(len(s_nums)-3):
            # skip same number
            if a > 0 and s_nums[a] == s_nums[a-1]:
                continue
            for b in range(a+1,len(s_nums)-2):
                # skip same number
                if b > a+1 and s_nums[b] == s_nums[b-1]:
                    continue

                # initialise 2 pointers 'c' and 'd'
                c = b+1
                d = len(s_nums)-1
                while c < d:
                    # skip same number
                    if c > b+1 and s_nums[c] == s_nums[c-1]:
                        c+=1
                        continue
                    # skip same number
                    if d < len(s_nums)-1 and s_nums[d] == s_nums[d+1]:
                        d-=1
                        continue

                    # check if sum = target and move pointer accordingly
                    sumz = s_nums[a]+s_nums[b]+s_nums[c]+s_nums[d]
                    if sumz == target:
                        result.append([s_nums[a],s_nums[b],s_nums[c],s_nums[d]])
                        c+=1
                    elif sumz < target:
                        c+=1
                    else:
                        d-=1

        return result

s = Solution()
print(s.fourSum( nums = [1,0,-1,0,-2,2], target = 0 ))      #  [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(s.fourSum( nums = [2,2,2,2,2], target = 8 ))          #  [[2,2,2,2]]
print(s.fourSum( nums = [-3,-2,-1,0,0,1,2,3], target = 0 )) #  [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(s.fourSum( nums = [-5,5,4,-3,0,0,4,-2], target = 4 )) #  [[-5,0,4,5],[-3,-2,4,5]]
