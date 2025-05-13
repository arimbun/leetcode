from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # generate parenthesis from 0 to n+1
        mem = [0] * (n+1)

        # base cases
        mem[0] = []
        mem[1] = ["()"]

        for i in range(2,n+1):
            result = set()

            # generate some parenthesis
            for j in range(i):
                for p in mem[i-1]:
                    result.add('('+p+')')

            # generate some more parenthesis
            for j in range(1,i):
                for p in mem[j]:
                    for q in mem[i-j]:
                        result.add(p+q)

            mem[i] = result

        return list(mem[n])

sol = Solution()
print(sol.generateParenthesis(1))
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(4))


["()()()()","((())())","()(()())","(()())()","(((())))","()(())()","(()(()))","((()()))","()()(())","(()()())","()((()))","((()))()","(())()()"]

["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
