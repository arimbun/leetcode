from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        mem = [[]] * (target+1)
        mem[0] = mem[1] = []
        for t in range(2,target+1):
            result = []
            for c in candidates:
                if c > t:   # we cannot go negative
                    break
                df = t-c
                memdf = mem[df]
                if not memdf and c == t:
                    # if this is the only element that meets target then
                    # add it to result as the sole element*
                    result.append([c])
                else:
                    # else append it to the list of existing elements
                    for e in memdf:
                        result.append(sorted(e+[c]))
            mem[t] = result

        # return only distinct list
        # use hashmap trick to eliminate dupes
        memt_map = {}
        memt = mem[target]

        for e in range(len(memt)):
            digits = memt[e]
            strz = ''
            for i in range(len(digits)):
                strz += str(digits[i])
                if i < len(digits)-1:
                    strz+='-'
            memt_map[strz] = digits

        return list(memt_map.values())


sol = Solution()
print(sol.combinationSum(candidates=[2,3,6,7], target=2))
print(sol.combinationSum(candidates=[2,3,6,7], target=7))
print(sol.combinationSum(candidates=[2,3,5], target=8))
print(sol.combinationSum(candidates=[3,5,8], target=11))
