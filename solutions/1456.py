class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # count substring from (0,k)
        countt = 0
        for i in range(k):
            if s[i] in ['a','e','i','o','u']:
                countt+=1

        # count substring (1,k+1), (2,k+2), etc. using sliding window
        a = 1
        b = a+k
        maxx = countt
        while b <= len(s):
            if k == 1:
                if s[a] in ['a','e','i','o','u']:
                    countt = 1
                else:
                    countt = 0
            else:
                if s[a-1] in ['a','e','i','o','u']:
                    countt -= 1
                if s[b-1] in ['a','e','i','o','u']:
                    countt += 1
            maxx = max(maxx, countt)
            a+=1
            b+=1

        return maxx

sol = Solution()
print(sol.maxVowels(s = "abciiidef", k = 3))
print(sol.maxVowels(s = "aeiou", k = 2))
print(sol.maxVowels(s = "tryhard", k = 4)) # 1
print(sol.maxVowels(s = "novowels", k = 1)) # 1
print(sol.maxVowels(s = "tnfazcwrryitgacaabwm", k = 4)) # 3
