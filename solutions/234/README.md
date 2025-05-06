# Approach

Let `x` be the resulting integer from the conversion. Loop through the Roman numeral string back to front, incrementing `x` by the Roman numeral that the program finds. Since iteration starts from the end of the string, it becomes very easy to detect subtraction. For example, a Roman numeral `XIV` would be processed by the algorithm as `5 - 1 + 10` which is equal to `14`. Subtraction detection is made possible by storing a reference to the previous numeral (variable `prev` in my code below) and checking if the current numeral (`c`) can be subtracted from the previous numeral (`prev`) as according to subtraction conditions.

In a simpler case without subtraction e.g. `XVIII`, the program would simply process this as `1 + 1 + 1 + 5 + 10`.

# Complexity

- Time complexity:

$$O(n)$$ where $$n$$ is the length of the Roman numeral string.

- Space complexity:

$$O(1)$$ 

# Code
```
class Solution {
public:
    int romanToInt(string s) {
        int x = 0, c = 0;
        int prev = 0;

        for (int i = s.size()-1; i >= 0; i--) {
            switch (s[i]) {
                case 'M':
                    c = 1000;
                    x += c;
                    break;
                case 'D':
                    c = 500;
                    x += c;
                    break;
                case 'C':
                    c = 100;
                    if (prev == 500 || prev == 1000) x -= c;
                    else x += c;
                    break;
                case 'L':
                    c = 50;
                    x += c;
                    break;
                case 'X':
                    c = 10;
                    if (prev == 50 || prev == 100) x -= c;
                    else x += c;
                    break;
                case 'V':
                    c = 5;
                    x += c;
                    break;
                case 'I':
                    c = 1;
                    if (prev == 5 || prev == 10) x--;
                    else x++;
                    break;
                default:
                    break;
            }
            prev = c;
        }

        return x;
    }
};
```