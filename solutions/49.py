from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for strz in strs:
            chars = []
            sorted_strz = sorted(strz)
            for c in sorted_strz:
                chars.append(c)

            key = ''
            for c in chars:
                key+=c

            if key not in groups:
                groups[key] = []
            groups[key].append(strz)

        result = []
        for k in groups.keys():
            result.append(groups[k])

        return result

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs)) # [["bat"],["nat","tan"],["ate","eat","tea"]]
