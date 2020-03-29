"""
322. Coin Change
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that 
amount. If that amount of money cannot be made up by any combination of the coins, 
return -1.
"""
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [0] + [float('inf')] * amount
    for c in coins:
        for i in range(coin, amount+1):
            """
            dp[i-c] is the amount of coins it takes for
            the value of the amount left over after you
            take a coin away. You add one to this because you 
            will have to add one more coin(c) to dp[i].
            """
            dp[i] = min(dp[i], dp[i-c] +1)
    return dp[-1] if dp[-1] != float('inf') else -1