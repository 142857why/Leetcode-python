class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x < y:
            return y - x
        dp = [0] * (x + 1)
        for i in range(y + 1):
            dp[i] = y - i

        for i in range(y + 1, x + 1):
            q5, r5 = divmod(i, 5)
            q11, r11 = divmod(i, 11)

            candidate1 = i - y
            candidate2 = (5 - r5 + 1) + dp[q5 + 1]
            candidate3 = (11 - r11 + 1) + dp[q11 + 1]
            candidate4 = (r5 + 1) + dp[q5]
            candidate5 = (r11 + 1) + dp[q11]
            dp[i] = min(candidate1, candidate2, candidate3, candidate4, candidate5)

        return dp[x]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumOperationsToMakeEqual(26, 1))
    print(sol.minimumOperationsToMakeEqual(54, 2))
    print(sol.minimumOperationsToMakeEqual(25, 30))
