class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x for x in s.split(' ') if x != ''][::-1])


sol = Solution()
print(sol.reverseWords("  hello world  "))
