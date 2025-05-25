class Solution:
    def removeStars(self, s: str) -> str:
        stk = 0

        ns = ''
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if c == '*':
                stk+=1
            elif stk>0 and c!='*':
                stk-=1
            else:
                ns+=c

        return ns[::-1]

sol = Solution()
print(sol.removeStars(s="leet**cod*e"))
print(sol.removeStars(s="erase*****"))
