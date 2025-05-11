from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        maps = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u', 'v'],
            '9': ['w','x','y','z'],
        }

        nmaps = []
        for d in digits:
            nmaps.append(maps[d])

        result = []
        for i in nmaps[0]:
            if len(nmaps) < 2:
                    nmaps.append([''])
            for j in nmaps[1]:
                if len(nmaps) < 3:
                    nmaps.append([''])
                for k in nmaps[2]:
                    if len(nmaps) < 4:
                        nmaps.append([''])
                    for l in nmaps[3]:
                        ss = i+j+k+l
                        result.append(ss)

        return result

digits = '235'
s = Solution()
print(s.letterCombinations(digits))
