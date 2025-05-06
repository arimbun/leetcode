from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # base case - exactly 0 coin needed to sum to 0
        if amount == 0:
            return 0

        sorted_coins = sorted(coins)
        minCoinsMatrix = [float('inf') for x in range(amount+1)]
        minCoinsMatrix[0] = 0

        # build min number of coins to get to amt = 1 all the way to
        # amt = amount
        for amt in range(1, amount+1):
            # print(amount_i)
            for j in range(len(sorted_coins)):
                val = sorted_coins[j]
                if val > amt:
                    break
                diff = amt - val

                if diff == 0:
                    # diff < 0 - exactly 1 coin needed to to sum to amount_i
                    minCoinsMatrix[amt] = 1
                elif diff < 0:
                    # diff < 0 - not possible to sum to amount_i
                    minCoinsMatrix[amt] = -1
                else:
                    # diff > 0
                    if minCoinsMatrix[diff] == -1:
                        minCoinsMatrix[amt] = -1
                    else:
                        minCoinsMatrix[amt] = min(1 + minCoinsMatrix[diff], minCoinsMatrix[amt])
                        # print("minCoinsMatrix[amount_i]", minCoinsMatrix[amount_i], end=" | ")

        # post-processing - set any amount that is still infinite to -1
        minCoinsMatrix = [-1 if x == float('inf') else x for x in minCoinsMatrix]

        return minCoinsMatrix[amount]



coins1 = [1,2,5]
amount1 = 11
coins2 = [2]
amount2 = 3
coins3 = [1]
amount3 = 0
coins4 = [186,419,83,408]
amount4 = 6249

sol = Solution()
res1 = sol.coinChange(coins1, amount1)
res2 = sol.coinChange(coins2, amount2)
res3 = sol.coinChange(coins3, amount3)
res4 = sol.coinChange(coins4, amount4)

print(res1) # 3
print(res2) # -1
print(res3) # 0
print(res4) # 20
