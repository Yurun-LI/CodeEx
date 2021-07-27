from typing import List


class Solution:
    def maxPoint(self, point: List[List[int]]) -> int:
        # f[i][j] = max(f[i-1][k]-abs(j-k) + point[i][j])
        dp = point[0]
        m = len(point)
        n = len(point[0])
        for i in range(1, m):
            new_dp = list(dp)
            left_max = -float('inf')
            right_max = -float('inf')
            for j in range(n):
                left_max = max(left_max, dp[j] + j)
                right_max = max(right_max, dp[n-1-j]-(n-1-j))
                new_dp[j] = max(left_max - j + point[i][j], new_dp[j])
                new_dp[n-1-j] = max(right_max + (n-1-j) +
                                    point[i][n-1-j], new_dp[n-1-j])
            dp = new_dp
        return max(dp)


point = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
print(Solution().maxPoint(point))


