"""
62. Unique Paths
A robot is located at the top-left corner of a 
m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid 
(marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

def uniquePaths(self, m: int, n: int) -> int:
    dp = [[1] * m] * n
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            """
            The current cell's number of paths is equal to the
            number of paths of the one above it plus the number
            of paths of the one to the left of it.
            """
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]