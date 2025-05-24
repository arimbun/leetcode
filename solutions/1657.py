
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """For this function to return True, the following conditions must be
        True:
        - word1 length = word2 length
        - same letters/characters appear in both word1 and word2
        - the frequencies (number of appearances) of characters in both word1
          and word2 is the same
        """
        # compare length
        if len(word1) != len(word2):
            return False

        # build letter count
        letters1 = {}
        for c in word1:
            if c not in letters1:
                letters1[c] = 0
            letters1[c] += 1

        letters2 = {}
        for c in word2:
            if c not in letters2:
                letters2[c] = 0
            letters2[c] += 1

        # compare
        k1 = sorted(list(letters1.keys()))
        k2 = sorted(list(letters2.keys()))
        v1 = sorted(list(letters1.values()))
        v2 = sorted(list(letters2.values()))
        if k1 != k2 or v1 != v2:
            return False

        return True

sol = Solution()
print(sol.closeStrings(word1 = "abc", word2 = "bca"))
print(sol.closeStrings(word1 = "a", word2 = "aa"))
print(sol.closeStrings(word1 = "cabbba", word2 = "abbccc"))
