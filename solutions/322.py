from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # base case: exactly 0 coin is needed to sum to 0
        if amount == 0:
            return 0

        # any other case:
        sorted_coins = sorted(coins)
        minCoinsMatrix = [float('inf') for x in range(amount+1)]
        minCoinsMatrix[0] = 0

        # build a matrix of coinChange starting from 1 all the way to amount
        for amt in range(1, amount+1):
            # consider every coin in the list
            for j in range(len(sorted_coins)):
                val = sorted_coins[j]   # value of current coin

                # value greater than amt? skip to next amt
                if val > amt:
                    break

                # else calculate difference after coin value is subtracted from
                # amount
                diff = amt - val
                if diff == 0:
                    # diff < 0: exactly 1 coin is needed to sum to amt
                    minCoinsMatrix[amt] = 1
                elif diff < 0:
                    # diff < 0: it is not possible to sum to amt
                    minCoinsMatrix[amt] = -1
                else:
                    # diff > 0: consider the min number of coins to sum to diff
                    if minCoinsMatrix[diff] == -1:
                        # if -1 then it is not possible to sum to amt
                        minCoinsMatrix[amt] = -1
                    else:
                        # if >= 0 then it is possible to sum to amt
                        # if the current # of coins needed is the minimum then set it to that
                        minCoinsMatrix[amt] = min(1 + minCoinsMatrix[diff], minCoinsMatrix[amt])

        # post-processing: set any amount in the matrix that is still infinite to -1
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
