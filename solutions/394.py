class Solution:
    def decodeString(self, s: str) -> str:
        result = ''
        i = 0
        times = 1
        digit_str = ''
        brackets = 0
        substrz = ''
        while i < len(s):
            c = s[i]
            if c.isdigit():
                if brackets > 0:
                    substrz+=c
                else:
                    digit_str+=c
                    if s[i+1] == '[':
                        times=int(digit_str)
            elif c == '[':
                if brackets > 0:
                    substrz+=c
                brackets+=1
            elif c == ']':
                brackets-=1
                if brackets == 0:
                    result+=times*self.decodeString(substrz)
                    substrz=''
                    digit_str=''
                    times=1
                else:
                    substrz+=c
            elif c.isalpha():
                if brackets > 0:
                    substrz+=c
                else:
                    result+=c
            i+=1

        return result

sol = Solution()
print(sol.decodeString(s = "3[a]2[bc]"))        # aaabcbc
print(sol.decodeString(s = "3[a2[c]]"))         # accaccacc
print(sol.decodeString(s = "2[abc]3[cd]ef"))    # abcabccdcdcdef
